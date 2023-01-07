from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name
