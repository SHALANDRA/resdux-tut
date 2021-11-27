from django.db import models

# Create your models here.
class team_login(models.Model):
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    updated_date=models.DateTimeField(null=True,blank=True)
    access=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)