from django.db import models

class OilProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=2500)
    category = models.CharField(max_length=50, default="Groundnut")
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.category}"
