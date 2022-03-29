
from django.shortcuts import render, redirect
from django.contrib.auth import (
							authenticate,
							get_user_model,
							login,
							logout
							)

from account.forms import (
		StaffRegistrationForm,
		StudentRegistrationForm,
	)

from account.models import Lecturer, Student

User = get_user_model()

def staff_register_view(request):

	form = StaffRegistrationForm()

	if request.method == "POST":
		form = StaffRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			staff_id 			= form.cleaned_data.get('staff_id') 
			firstname 			= form.cleaned_data.get('firstname') 
			lastname 			= form.cleaned_data.get('lastname') 
			password 			= form.cleaned_data.get('password1') 
			email 				= form.cleaned_data.get('email') 
			image 				= form.cleaned_data.get('image') 

			queryset 			= User.objects.filter(username__iexact=staff_id)



			# try:
			# 	if queryset.exists():
			# 		print(form.errors)

			# except:
			# 	pass

			user 				= User()
			user.username 		= staff_id
			user.first_name 	= firstname
			user.last_name 		= lastname
			user.email 			= email
			user.is_staff 		= True
			user.set_password(password)
			user.save()

			staff 				= Lecturer(
										staff_id=staff_id,
										firstname=firstname,
										lastname=lastname,
										email=email,
										image=image
										)

			staff.user 			= user 
			staff.save()

	return render(request, 'account/staff_register.html', dict(form=form))
			

def student_register_view(request):

	form = StudentRegistrationForm()

	if request.method == "POST":
		form = StudentRegistrationForm(request.POST, request.FILES)
		if form.is_valid():
			matric_no 			= form.cleaned_data.get('matric_no') 
			firstname 			= form.cleaned_data.get('firstname') 
			lastname 			= form.cleaned_data.get('lastname') 
			password 			= form.cleaned_data.get('password1') 
			email 				= form.cleaned_data.get('email') 
			image 				= form.cleaned_data.get('image') 

			queryset 			= User.objects.filter(username__iexact=matric_no)

			try:
				if queryset.exists():
					print(form.errors)

			except:
				pass

			user 				= User()
			user.username 		= matric_no
			user.first_name 	= firstname
			user.last_name 		= lastname
			user.email 			= email
			user.set_password(password)
			user.save()

			student 			= Student(
										matric_no=matric_no,
										firstname=firstname,
										lastname=lastname,
										email=email,
										image=image
										)

			student.user 		= user 
			student.save()

	return render(request, 'account/student_register.html', dict(form=form))



def login_view(request):

	if request.method == "POST":
		username = request.POST.get('id')
		password = request.POST.get('password')

		user  = authenticate(
							request,
							username=username,
							password=password
							)
		if user is not None:
			login(request, user)
			return redirect('dashboard:dashboard')

	return render(request, 'account/login.html')



def logout_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		logout(request)
		return redirect('account:login')


