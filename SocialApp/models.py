from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"


class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    # image = models.ImageField(upload_to='profilePictures')
    image = models.ImageField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title
