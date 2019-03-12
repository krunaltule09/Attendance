from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Student(models.Model):
	user              =models.ForeignKey(User,on_delete=models.CASCADE)
	first_name        =models.CharField(max_length=255,blank=True)
	last_name         =models.CharField(max_length=255,blank=True)
	panel             =models.IntegerField()
	roll_number       =models.IntegerField(null=False,blank=False,unique=True)
	att_os            =models.IntegerField(blank=True,null=True)
	att_ds2           =models.IntegerField(blank=True,null=True)
	att_sepm          =models.IntegerField(blank=True,null=True)
	att_mmc           =models.IntegerField(blank=True,null=True)
	att_ic            =models.IntegerField(blank=True,null=True)


	def __str__(self):
		return str(self.roll_number)