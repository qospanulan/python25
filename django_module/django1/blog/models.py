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


# Post
# - content
# - blog
# - comments
# - likes
