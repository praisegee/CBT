from django import forms

from tests.models import Question

class QuestionForm(forms.Form):

	DURATION 			=  ((20, 20),
							(25, 25),
							(30, 30),
							(35, 35),
							(40, 40),
							(45, 45),
							(50, 50))

	course_title 		= forms.CharField(max_length=100)
	course_code 		= forms.CharField(max_length=100)
	instruction 		= forms.CharField(widget=forms.Textarea)
	no_of_question 		= forms.CharField(widget=forms.NumberInput)
	minite_to_finish 	= forms.IntegerField(widget=forms.Select(choices=DURATION))
	test_date			= forms.DateTimeField(widget=forms.DateTimeInput)
	file 				= forms.FileField()



