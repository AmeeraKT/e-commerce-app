from django.db import models

class Product(models.Model):
    nameclass = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    #@property
    #def is_mood_strong(self):
    #    return self.mood_intensity > 5