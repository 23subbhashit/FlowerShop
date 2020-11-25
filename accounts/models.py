from django.db import models

# Create your models here.
# models.py 
class Img(models.Model): 
    name = models.CharField(max_length=50) 
    Main_Img = models.ImageField(upload_to='images/')
    price = models.IntegerField(default=0)