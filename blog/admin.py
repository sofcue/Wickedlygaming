from django.contrib import admin
from .models import Post, Videos, Comment
from embed_video.admin import AdminVideoMixin


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Videos, MyModelAdmin)
