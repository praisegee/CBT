
from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):
	
	def create_user(self, username, email, password=None):
		if not username:
			raise ValueError("Please provide an ID for the user!")
		if not email:
			raise ValueError("User must have an email!")
		if not password:
			raise ValueError("Please provide a password for the user!")

		user = self.model(
				username=username,
				email=self.normalize_email(email)
			)
		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_superuser(self, username, email, password):

		user = self.create_user(
				username=username,
				email=self.normalize_email(email),
				password=password
			)
		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)

		return user



class User(AbstractUser):
	username = models.CharField(max_length=100, unique=True, editable=True, primary_key=True)
	is_admin = models.BooleanField(default=False)
	is_lecturer = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)


	def __str__(self):
		return self.username

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']



