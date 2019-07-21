from django.db import models
class regandlogindata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()