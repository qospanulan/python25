from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.id})"


class Post(models.Model):
    content = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content[:15]}... ({self.id})"
