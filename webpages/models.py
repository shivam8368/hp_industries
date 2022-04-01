from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Latest_work(models.Model):
    photo = models.ImageField(upload_to = 'media/latest_work/%Y/%m/')
    photo_desc = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.photo_desc



class Team(models.Model):

    team_photo = models.ImageField(upload_to = 'media/team/%Y/%m/')
    team_name = models.CharField(max_length=255)
    team_position = models.CharField(max_length=255)
    team_email = models.EmailField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name

