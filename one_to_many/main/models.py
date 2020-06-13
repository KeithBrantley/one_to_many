from django.db import models

# Create your models here.

class Chef(models.Model):
    name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    name = models.CharField(max_length=255)
    tastiness_level = models.IntegerField()
    spice = models.IntegerField()
    maker = models.ForeignKey(Chef, related_name="dishes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)