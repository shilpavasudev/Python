from unittest.util import _MAX_LENGTH
from django.db import models




class Signup(models.Model):
   Id= models.IntegerField(default = 0, null=False)
   Name = models.CharField(max_length = 255)
   Contact = models.EmailField(max_length = 50)
   Address = models.CharField(max_length= 255)
   
   
   def __str__(self):
       return f"{self.Id} {self.Name}"

class Login(models.Model):
   Username= models.CharField(max_length = 255)
   password = models.CharField(max_length = 255)
   
   def __str__(self):
        return f"{self.Username}"


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    studentname = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.studentname}"


    
