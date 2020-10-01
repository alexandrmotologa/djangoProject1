from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    image = models.CharField(max_length=255)
    done = models.BooleanField()

    def __str__(self):
        return "PRODUCT " + self.name + "(" + self.done + ")"