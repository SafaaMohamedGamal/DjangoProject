from django.contrib import admin
from .models import comments, replys, likes, Categories, Post
# Register your models here.
# admin.site.register(poststable)
admin.site.register(comments)
admin.site.register(replys)
admin.site.register(likes)
admin.site.register(Categories)
admin.site.register(Post)