from django.db.models import QuerySet

from blog.models import Blog, Post


class BlogService:

    def get_all_blogs(self) -> list[Post]:

        blogs: QuerySet[Blog] = Blog.objects.all()
        # blogs: QuerySet[Blog] = Blog.objects.filter(
        #     ~Q(status=HIDDEN)
        # )

        return blogs

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

        blog: Blog = Blog.objects.get(id=blog_id)

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
