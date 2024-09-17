from django.db import models
class employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
