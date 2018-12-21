#coding:utf-8

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    """Tag 标签"""
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})


