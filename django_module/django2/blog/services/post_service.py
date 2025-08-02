from functools import lru_cache

from blog.models import Post


class PostService:

    def get_all_posts(self) -> Post:

        posts = Post.objects.all()

        return posts

    def get_all_posts_by_blog_id(self, blog_id: int) -> Post:

        posts = Post.objects.filter(blog_id=blog_id)

        return posts

    def create_post(
            self,
            blog_id: int,
            author_id: int,
            content: str
    ) -> Post:

        post = Post.objects.create(
            content=content,
            blog_id=blog_id,
            author_id=author_id
        )
        return post


@lru_cache
def get_post_service() -> PostService:
    print("get_post_service called!")
    return PostService()
