from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pis')
    desc=models.TextField()
def __str__(self):
    return self.name
class team(models.Model):
    person=models.CharField(max_length=250)
    pimg=models.ImageField(upload_to='pis2')
    tdesc=models.TextField()
def __str__(self):
    return self.person