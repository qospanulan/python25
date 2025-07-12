from django.db import models

# Django ORM - SQLAlchemy ORM

# User

# Blog
# - name
# - description
# - author *
# - followers *
# - posts *

# create table Blog (
#   name varchar(120),
#   desc...
#   created_at TIMESTAMP
# )

class Blog(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.id})"


# Post
# - content
# - blog
# - comments
# - likes

class Post(models.Model):
    content = models.TextField(verbose_name="Контент")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Блог")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content[:15]}... ({self.id})"
