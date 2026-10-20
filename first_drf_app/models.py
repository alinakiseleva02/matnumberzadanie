from django.db import models

class Number(models.Model):
    value = models.IntegerField() 
    name = models.CharField(max_length=255) 
    discoverer = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.name