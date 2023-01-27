from django.db import models

# Create your models here.

class Uavs(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
    model = models.CharField(max_length=20)
    model_no = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.summary
        return self.model
        return self.model_no
        return self.price
        return self.category
        return self.weight
        return self.brand