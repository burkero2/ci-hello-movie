from django.db import models


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    director = models.CharField(max_length=50, null=False, blank=False)
    genre = models.CharField(max_length=50, blank=False)
    summary = models.TextField(max_length=400, null=False, blank=True)
    score = models.IntegerField(null=False, blank=False)
    watched = models.BooleanField(null=False, blank=False, default=False)

    
    def __str__(self):
        return f"{self.title}: {self.director}"
