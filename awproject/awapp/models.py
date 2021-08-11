from django.db import models

# Create your models here.
class awapp(models.Model):
    mainphoto = models.ImageField(blank=True, null=True)
    postname = models.CharField(max_length=200)
    contents = models.TextField()
    