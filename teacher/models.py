from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Teacher(models.Model):
    user              =models.ForeignKey(User,on_delete=models.CASCADE)
    first_name        =models.CharField(max_length=255,blank=True)
    last_name         =models.CharField(max_length=255,blank=True)
    subject           =models.CharField(max_length=20)

    
    def __str__(self):
        return str(self.user)

