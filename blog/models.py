

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from embed_video.fields import EmbedVideoField

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updatedOn = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/', blank=True)


    class Meta:
        ordering = ['-createdOn']

    def __str__(self):
        return self.title


class Videos(models.Model):
    name = models.CharField(max_length=100, unique=True)
    video = EmbedVideoField()  # same like models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Videos"


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)