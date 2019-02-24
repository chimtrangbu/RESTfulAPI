from django.db import models

# Create your models here.
class Movie(models.Model):
    """
    Movie Model
    Defines the attributes of a movie
    """
    Title = models.CharField(max_length=255)
    Rated = models.CharField(max_length=255)
    imdbID = models.CharField(max_length=255)
    imdbRating = models.CharField(max_length=255)