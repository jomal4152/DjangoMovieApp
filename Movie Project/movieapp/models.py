from django.db import models


# Create your models here.

class movie_details(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
