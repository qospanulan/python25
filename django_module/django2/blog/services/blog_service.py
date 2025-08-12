from functools import lru_cache

from django.conf import settings
from django.db.models import QuerySet
# from rest_framework.pagination import PageNumberPagination

from blog.models import Blog, Post
from blog.paginations import CustomPagePagination


class BlogService:

    def get_all_blogs(
            self,
            author_ids: list[int] | None,
            name: str | None,
            page: int = 1,
            page_size: int | None = None
            # url: str = ""
    ) -> dict:

        blogs: QuerySet[Blog] = Blog.objects.all().select_related("author")

        if author_ids:
            blogs = blogs.filter(
                author_id__in=author_ids
            )
        if name:
            blogs = blogs.filter(
                name=name
            )

        if not page_size:
            page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE", 3)

        bottom = (page - 1) * int(page_size)
        top = bottom + int(page_size)
        blogs = blogs.order_by("created_at")[bottom:top]
        blog_count = Blog.objects.all().count()

        # paginator = CustomPagePagination(
        #     page=page,
        #     url=url
        # )

        # blogs = paginator.paginate_queryset(
        #     queryset=blogs
        # )

        result_data = {
            'count': blog_count,
            # 'count': paginator.page.paginator.count,
            # 'next': paginator.get_next_link(),
            # 'previous': paginator.get_previous_link(),
            'results': blogs,
        }

        return result_data

    def create_blog(
            self,
            user_id: int,
            data: dict
    ) -> Blog:
        # blog = Blog(
        #     name=data.get('name'),
        #     description=data.get('description'),
        #     tags=data.get('tags')
        # )

        blog = Blog(
            author_id=user_id,
            name=data.get('name'),
            description=data.get('description')
        )

        blog.save()

        blog.tags.set(data.get('tags'))  # tags = objects

        return blog

    def get_blog_by_id(self, blog_id: int) -> Blog:
        blog: Blog = (
            Blog.objects
            .prefetch_related("post_set", "tags")
            .select_related("author")
            .get(id=blog_id)
        )

        return blog

    def update_blog(
            self,
            blog_id: int,
            data: dict
    ) -> Blog:
        blog: Blog = Blog.objects.get(id=blog_id)

        for key, value in data.items():
            setattr(blog, key, value)

        blog.save()

        return blog

    def update_status(
            self,
            blog_id: int,
            new_status: str
    ) -> Blog:
        blog: Blog = Blog.objects.get(id=blog_id)

        blog.status = new_status

        blog.save()

        return blog

    def delete_blog(self, blog_id: int) -> None:
        blog: Blog = Blog.objects.get(id=blog_id)

        blog.delete()


@lru_cache
def get_blog_service() -> BlogService:
    return BlogService()
