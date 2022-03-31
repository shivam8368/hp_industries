from django.db import models

# Create your models here.

class Latest_work(models.Model):
    photo = models.ImageField()
    

    def __str__(self):
        return self.first_name