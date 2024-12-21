from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    quantity = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.JSONField(null=True, blank=True)  # Updated to allow null/empty values
    instructions = models.TextField()
    is_favorite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)

    def __str__(self):
        return self.title

