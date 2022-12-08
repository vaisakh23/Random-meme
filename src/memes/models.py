from django.db import models

# Create your models here.
class Meme(models.Model):
    time = models.TimeField(auto_now=True)
    img_url = models.CharField(max_length=140)
