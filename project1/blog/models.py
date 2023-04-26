from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    content = models.TextField()
    update_date = models.DateTimeField()
    published_date = models.DateTimeField()