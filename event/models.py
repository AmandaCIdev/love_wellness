from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(max_length=200,)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts", null=True)
    content = models.TextField(null=True)
    published_on = models.DateTimeField(auto_now_add=True, null=True)
    image = CloudinaryField('image', blank=True)
    likes = models.ManyToManyField (User, related_name = 'event_post')
