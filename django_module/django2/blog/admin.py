from django.contrib import admin

from blog.models import Blog, Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'content', 'blog_id', 'author_id')
    list_display_links = ('__str__', 'id')
    list_filter = ('author_id', 'blog_id')
    search_fields = ('content',)
    # list_editable = ('content',)


admin.site.register(Blog)
# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
