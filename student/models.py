from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Panel 


User=get_user_model()

class Student(models.Model):
	user              =models.OneToOneField(User,on_delete=models.CASCADE)
	first_name        =models.CharField(max_length=255,blank=True)
	last_name         =models.CharField(max_length=255,blank=True)
	panel             =models.ForeignKey(Panel,on_delete=models.CASCADE)
	roll_number       =models.IntegerField(null=False,blank=False,unique=True)
	att_os            =models.IntegerField(blank=True,null=True)
	att_ds2           =models.IntegerField(blank=True,null=True)
	att_sepm          =models.IntegerField(blank=True,null=True)
	att_mmc           =models.IntegerField(blank=True,null=True)
	att_ic            =models.IntegerField(blank=True,null=True)


	def __str__(self):
		return str(self.roll_number)

# class Subject(models.Model):
# 	subject_name = models.CharField(max_length=25,blank=False)
# 	subject_code = modeis.CharField(max_length=8,blank=False,unique=True)