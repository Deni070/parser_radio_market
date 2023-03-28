from django.db import models
from django.contrib.auth.models import AbstractUser

#class Story_Segment
class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='img/')
    file = models.FileField(
        upload_to='music/',
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
