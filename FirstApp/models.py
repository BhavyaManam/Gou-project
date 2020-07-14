from django.db import models
from django import forms 
# Create your models here.
class MOU(models.Model):
	
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	dob = models.DateField(null=True)
	mobile= models.IntegerField(null=True)
	img=models.ImageField(upload_to='profilepics/',null=True)
	mailid  = models.EmailField(max_length=50)
	password=models.CharField(max_length=20)
	
	def __str__(self):
		return self.mailid

 

