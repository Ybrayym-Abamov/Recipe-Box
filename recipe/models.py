from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    instructions = models.TextField()

    def __str__(self):
        return self.title
