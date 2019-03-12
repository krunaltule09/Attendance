
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
	def create_user(self,email,username,password=None,is_admin=False,is_staff=False,is_verified=False,is_active=True):
		if not email:
			raise ValueError("email id is required")

		if not username:
			raise ValueError("username is required")


		if not password:
			raise ValueError("password must require")

		user_obj=self.model(
			email=self.normalize_email(email)
			
			
			)
		user_obj.username=username
		user_obj.set_password(password)
		user_obj.admin=is_admin
		user_obj.verified=is_verified
		user_obj.staff=is_staff
		user_obj.active=is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self,email,username,password=None):
		user=self.create_user(
			email,
			username,
			password=password,

			is_admin=False,
			is_staff=True
			)
		return user

	def create_superuser(self,email,username,password=None):
		user=self.create_user(
			email,
			username,	
			password=password,
		
			is_admin=True,
			is_staff=True,
			is_verified=True
			)
		return user






class User(AbstractBaseUser):
	username=models.CharField(max_length=255,unique=True)
	email=models.EmailField(max_length=255,unique=True)
	active=models.BooleanField(default=True)
	admin=models.BooleanField(default=False)
	staff=models.BooleanField(default=False)
	verified=models.BooleanField(default=False) #for verification purpose

	objects = UserManager()
	def get_full_name(self):
		return (self.email)

	def get_short_name(self):
		return self.email

	def get_username(self):
		return self.username

	def get_user_id(self):
		return self.id

	def has_perm(self,perm,obj=None):
		return True

	def has_module_perms(self,app_label):
		return True


	def __str__(self):
		return (self.email)

	USERNAME_FIELD="username"
	REQUIRED_FIELDS=['email']


	@property
	def is_active(self):
		return self.active
	
	@property
	def is_admin(self):
		return self.admin

	@property
	def is_verified(self):
		return self.verified

	@property
	def is_staff(self):
		return self.staff









