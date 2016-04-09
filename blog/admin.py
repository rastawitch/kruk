from django.contrib import admin
from .models import Post
#. przed models, bo to w tym samym pliku co admin, Post jest klasą
# Register your models here.
admin.site.register(Post)
