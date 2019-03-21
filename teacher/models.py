from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Subject,Panel


User=get_user_model()

class Teacher(models.Model):
    user              =models.OneToOneField(User,on_delete=models.CASCADE)
    panel             =models.ForeignKey(Panel,on_delete=models.CASCADE)
    first_name        =models.CharField(max_length=255,blank=True)
    last_name         =models.CharField(max_length=255,blank=True)
    subject           =models.ForeignKey(Subject,on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.user)

class SecretCode(models.Model):
    code               =models.CharField(max_length=12)
    teacher_username   =models.IntegerField(default=0,null=False,blank=False)
    date_time_created  =models.DateTimeField(auto_now_add=False)
    panel              =models.ForeignKey(Panel,on_delete=models.CASCADE)