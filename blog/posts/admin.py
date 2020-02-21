from django.contrib import admin
from .models import poststable, comments, replys, likes
# Register your models here.
admin.site.register(poststable)
admin.site.register(comments)
admin.site.register(replys)
admin.site.register(likes)