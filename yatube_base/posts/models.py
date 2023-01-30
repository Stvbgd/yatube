from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    
    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True,
                              null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text
