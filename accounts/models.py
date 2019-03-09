from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
	user       =models.OneToOneField(User,on_delete=models.CASCADE)
	firstname  =models.CharField(max_length=50,null=True,blank=True)
	lastname   =models.CharField(max_length=50,null=True,blank=True)
	panel      =models.IntegerField()



	def __str__(self):
		retrun(self.firstname+""+self.lastname)