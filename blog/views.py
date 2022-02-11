from blog.models import Blogpost
from django.shortcuts import render

# Create your views here.


def index(requests):

    posts = Blogpost.objects.all()

    return render(requests, "blog/index.html", {"posts": posts})


def blogpost(requests, id):
    post = Blogpost.objects.filter(id=id).first()
    prevId = id-1
    nextId = id+1
    prevPost = Blogpost.objects.filter(id=prevId).first()
    nextPost = Blogpost.objects.filter(id=nextId).first()

    return render(requests, "blog/blogpost.html", {"post": post, "prevPost": prevPost, "nextPost": nextPost})
