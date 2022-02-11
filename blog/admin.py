from django.contrib import admin

# Register your models here.
from .models import Blogpost


class adminBlogpost(admin.ModelAdmin):
    list_display = ("title",  "thumbnail", "publishedAt")


admin.site.register(Blogpost, adminBlogpost)
