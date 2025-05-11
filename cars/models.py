from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    mileage = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title