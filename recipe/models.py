from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(
        'RecipeItem',
        related_name='favorites_of',
        blank=True
    )

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
