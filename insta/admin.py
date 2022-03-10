from django.contrib import admin
from .models import Post,Profile, Comment,Likes

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Likes)

