from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    ram = models.IntegerField()
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.brand
    



