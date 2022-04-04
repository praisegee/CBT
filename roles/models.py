from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


# CREATE STAFF MODEL
class Lecturer(models.Model):
	staff_id 		= models.CharField(max_length=50, unique=True, primary_key=True)
	user 			= models.OneToOneField(User, on_delete=models.CASCADE) 
	email 			= models.EmailField(null=True, blank=True)
	image 			= models.ImageField(upload_to="staff", default="default.jpg")

	def __str__(self):
		return self.user.username

	@property
	def imageURL(self):
		try:
			img = self.image.url
		except:
			img = '/media/default.jpg'

		return img 


# CREATE STUDENT MODEL
class Student(models.Model):
	matric_no 		= models.CharField(max_length=50, unique=True, primary_key=True)
	user 			= models.OneToOneField(User, on_delete=models.CASCADE) 
	email 			= models.EmailField(null=True, blank=True)
	image 			= models.ImageField(upload_to="student", default="default.jpg")

	def __str__(self):
		return self.user.username

	@property
	def imageURL(self):
		try:
			img = self.image.url
		except:
			img = '/media/default.jpg'

		return img









