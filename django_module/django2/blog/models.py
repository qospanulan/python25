from django.contrib.auth import get_user_model
from django.db import models

from blog.constants import VISIBLE, HIDDEN, ARCHIVED


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

"""
class Blog_Tag():
    id = int
    
    blog_id = int
    tag_id = int

"""

class Blog(models.Model):

    STATUS_CHOICES = (
        (VISIBLE, "Visible"),
        (HIDDEN, "Hidden"),
        (ARCHIVED, "Archived")
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(Tag)

    name = models.CharField(max_length=120)
    description = models.TextField()

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=VISIBLE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Post(models.Model):

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    content = models.TextField()
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        # related_name="post_set" # {modelName}_set
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content[:15]}... ({self.id})"

    class Meta:
        # indexes = [
        #     models.Index(fields=['author_id', 'content'], name='post_author_content_idx'),
        # ]
        constraints = [
            models.UniqueConstraint(fields=['author_id', 'content'], name='post_author_content_unq_idx')
        ]

        verbose_name = "Пост" # "Category"
        verbose_name_plural = "Посты" # "Categories"


class Comment(models.Model):
    text = models.CharField(max_length=200)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    parent_comment = models.ForeignKey(
        "Comment",
        on_delete=models.CASCADE,
        related_name="replies",
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text[:10]}... ({self.pk}) for Post ID: {self.post_id}"

#
#
# Еда (1)
#  - replies = [2, 3]
#
# Топ 5 рецептов (2)
#  - parent_comment = 1
#
# Завтрак важен (3)
#  - parent_comment = 1
