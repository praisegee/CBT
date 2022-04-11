from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import (
							authenticate,
							get_user_model,
							login,
							logout
							)

from roles.forms import (
		StaffRegistrationForm,
		StudentRegistrationForm,
	)

from roles.models import Lecturer, Student

User = get_user_model()

def staff_register_view(request):
	form = StaffRegistrationForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		staff_id 			= form.cleaned_data.get('staff_id').upper() 
		firstname 			= form.cleaned_data.get('firstname') 
		lastname 			= form.cleaned_data.get('lastname') 
		password 			= form.cleaned_data.get('password1') 
		email 				= form.cleaned_data.get('email') 
		image 				= form.cleaned_data.get('image') 


		staff_queryset 		= User.objects.filter(username=staff_id)
		email_queryset 		= User.objects.filter(email=email)

		if staff_queryset.exists():
			messages.error(request, 'Staff Id already exist! Try again.')
			return redirect('account:staff-register')

		if email_queryset.exists():
			messages.error(request, 'Email already exist! Try again.')
			return redirect('account:staff-register')


		user 				= User()
		user.username 		= staff_id
		user.first_name 	= firstname
		user.last_name 		= lastname
		user.email 			= email
		user.is_lecturer 	= True
		user.set_password(password)
		user.save()

		staff 				= Lecturer(
									staff_id=staff_id,
									email=email,
									image=image
									)

		staff.user 			= user 
		staff.save()

		messages.success(request, 'Successfully registered!')

		return redirect('account:login')

	return render(request, 'account/staff_register.html', dict(form=form))
			



def student_register_view(request):

	context = {}
	form = StudentRegistrationForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		matric_no 			= form.cleaned_data.get('matric_no').upper()
		firstname 			= form.cleaned_data.get('firstname') 
		lastname 			= form.cleaned_data.get('lastname') 
		password 			= form.cleaned_data.get('password1') 
		email 				= form.cleaned_data.get('email') 
		image 				= form.cleaned_data.get('image') 


		matric_queryset 	= User.objects.filter(username=matric_no)
		email_queryset 		= User.objects.filter(email=email)

		if matric_queryset.exists():
			messages.error(request, 'Matric Number already exist! Try again.')
			return redirect('account:student-register')

		if email_queryset.exists():
			messages.error(request, 'Email already exist! Try again.')
			return redirect('account:student-register')


		user 				= User()
		user.username 		= matric_no
		user.first_name 	= firstname
		user.last_name 		= lastname
		user.email 			= email
		user.is_student 	= True
		user.set_password(password)
		user.save()

		student 			= Student(
									matric_no=matric_no,
									email=email,
									image=image
									)

		student.user 		= user 
		student.save()

		messages.success(request, 'Registration Successfull! Login to your dashboard.')

		return redirect('account:login')

	return render(request, 'account/student_register.html', dict(form=form))



def login_view(request):

	if request.method == "POST":
		username = request.POST.get('id').upper()
		password = request.POST.get('password')

		user  = authenticate(
							request,
							username=username,
							password=password
							)
		if user is not None:
			if user.is_student:
				login(request, user)
				return redirect('dashboard:student:tests')
			elif user.is_lecturer:
				login(request, user)
				return redirect('dashboard:lecturer:questions')
		else:
			messages.error(request, 'Invalid Credentials. Try again!')

	return render(request, 'account/login.html')



def logout_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		logout(request)
		return redirect('account:login')


