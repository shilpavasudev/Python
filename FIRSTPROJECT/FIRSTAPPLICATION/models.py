from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Signup(models.Model):
    Name = models.CharField(max_length = 255)
    Contact = models.EmailField(max_length = 50)
    Address = models.CharField(max_length= 255)
    
    
    def __str__(self):
        return f"{self.id} {self.Name}"






    