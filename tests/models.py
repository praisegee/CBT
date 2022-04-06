from django.db import models

from roles.models import Lecturer

class Question(models.Model):
	DURATION = (
			(20, 20),
			(25, 25),
			(30, 30),
			(35, 35),
			(40, 40),
			(45, 45),
			(50, 50),
		)
	lecturer 			= models.ForeignKey(Lecturer, on_delete=models.CASCADE)
	course_title 		= models.CharField(max_length=100, blank=True, null=True)
	course_code 		= models.CharField(max_length=100, blank=True, null=True)
	instruction 		= models.TextField(max_length=1000, blank=True, null=True)
	no_of_question 		= models.IntegerField(blank=True, null=True)
	minite_to_finish 	= models.IntegerField(default=20, choices=DURATION)
	is_done 			= models.BooleanField(default=False)
	test_date 			= models.DateTimeField(blank=True, null=True)
	file 				= models.FileField(upload_to="questions", blank=True, null=True)
	date_created 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.course_code).upper()
