

# Create your models here.

from django.conf import settings
from django.db import models

from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='myapp/media/')

    def __str__(self):
        return self.title

import os

from django.db import models


def upload_path(instance, filename):
    # change the filename here is required
    return os.path.join("uploads", filename)


class ImageModel(models.Model):
    image = models.ImageField(upload_to="media", null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True, auto_now_add=True)

