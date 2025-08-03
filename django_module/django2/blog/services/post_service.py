from functools import lru_cache

from blog.models import Post
from blog.services.blog_service import BlogService, get_blog_service


class PostService:

    def __init__(
            self,
            blog_service: BlogService
    ):
        self.blog_service = blog_service

    def get_all_posts(self) -> Post:

        posts = Post.objects.all().select_related("author", "blog")

        return posts

    def get_all_posts_by_blog_id(self, blog_id: int) -> Post:

        posts = Post.objects.filter(blog_id=blog_id).select_related("author", "blog")

        return posts

    def create_post(
            self,
            blog_id: int,
            author_id: int,
            content: str
    ) -> Post:

        blog = self.blog_service.get_blog_by_id(
            blog_id=blog_id
        )

        if author_id != blog.author.id:
            raise Exception("Автор пост может создать только под своим блогом.")

        post = Post.objects.create(
            content=content,
            blog_id=blog_id,
            author_id=author_id
        )
        return post


@lru_cache
def get_post_service() -> PostService:
    return PostService(
        blog_service=get_blog_service()
    )
