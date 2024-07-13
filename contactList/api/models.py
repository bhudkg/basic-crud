from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40)
    number = models.CharField(unique=True, blank=False, max_length=13)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name
    


