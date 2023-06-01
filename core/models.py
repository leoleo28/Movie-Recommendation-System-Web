from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=1000)

    def __str__(self):
        return self.name
        
class MovieFilter(models.Model):
    name=models.CharField(max_length=1000)
    rate=models.CharField(max_length=100)
    runtime=models.IntegerField(default=0)
    year=models.CharField(max_length=100)
    genres=models.CharField(max_length=100)
    poster=models.CharField(max_length=10000, default='')
    overview=models.CharField(max_length=1000000, default='')
    def __str__(self):
        return self.name
