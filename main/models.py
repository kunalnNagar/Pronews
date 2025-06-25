from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = 'categories'

class News(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    publish = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/')
    desc = models.TextField()


    class Meta:
        verbose_name_plural = 'News'

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "comment"