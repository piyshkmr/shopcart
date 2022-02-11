from django.db import models
from django.db.models.fields import AutoField, CharField, DateField
from django.db.models.fields.files import ImageField

# Create your models here.


class Blogpost (models.Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=200)
    h1 = CharField(max_length=500)
    p1 = CharField(max_length=5000)
    h2 = CharField(max_length=500)
    p2 = CharField(max_length=5000)
    h3 = CharField(max_length=500)
    p3 = CharField(max_length=5000)
    publishedAt = DateField(auto_now_add=True)
    thumbnail = ImageField(upload_to="blog/images")

    def __str__(self):
        return self.title
