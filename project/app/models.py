from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    
class Query(models.Model):
    Email=models.EmailField()
    Queryl=models.CharField(max_length=100)
    
    
    