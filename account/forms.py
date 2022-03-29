from django import forms 
from django.contrib.auth.forms import UserCreationForm
from account.models import Lecturer, Student
from django.contrib.auth import get_user_model


User = get_user_model()


class AdminRegistrationForm(UserCreationForm):
	username = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		


class StaffRegistrationForm(forms.Form): 
	staff_id 		= forms.CharField(max_length=50, required=True)
	firstname 		= forms.CharField(max_length=100)
	lastname 		= forms.CharField(max_length=100)
	password1 		= forms.CharField(label="Create Password", widget=forms.PasswordInput)
	password2 		= forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
	email 			= forms.EmailField()
	image 			= forms.ImageField()


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')	
		password2 = self.cleaned_data.get('password2')	

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password don't match!")
		return password1

	def clean_staff_id(self):
		staff_id 	= self.cleaned_data.get('staff_id')
		queryset 	= Lecturer.objects.filter(staff_id__iexact=staff_id)

		if queryset.exists():
			raise forms.ValidationError("User already exist!")
		return staff_id
		

class StudentRegistrationForm(forms.Form):
	matric_no 		= forms.CharField(max_length=50, required=True)
	firstname 		= forms.CharField(max_length=100)
	lastname 		= forms.CharField(max_length=100)
	password1 		= forms.CharField(label="Create Password", widget=forms.PasswordInput)
	password2 		= forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
	email 			= forms.EmailField()
	image 			= forms.ImageField()


	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')	
		password2 = self.cleaned_data.get('password2')	

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Password don't match!")
		return password1

	def clean_matric_no(self):
		matric_no 	= self.cleaned_data.get('matric_no')
		queryset 	= Lecturer.objects.filter(staff_id__iexact=matric_no)

		if queryset.exists():
			raise forms.ValidationError("User already exist!")
		return matric_no




