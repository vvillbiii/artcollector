from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    period = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Painting(models.Model):
    name = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    year = models.IntegerField(default=1800)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="paintings")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Article(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Collection(models.Model):
    name = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    paintings = models.ManyToManyField(Painting)

    def __str__(self):
        return self.name