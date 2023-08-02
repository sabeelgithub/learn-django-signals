from django.db import models
from django.contrib.auth.models import User 

# Create your models here



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)



