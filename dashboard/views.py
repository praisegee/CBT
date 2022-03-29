from django.shortcuts import render



def user_dashboard(request, *args, **kwargs):
	user = request.user
	context = {}

	if user.is_student:
		return student_dashboard(request)

	if user.is_lecturer:
		return lecturer_dashboard(request)

	return render(request, 'dashboard/dashboard.html', context)





def admin_dashboard(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/admin-dashboard.html', context)


def lecturer_dashboard(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/lecturer-dashboard.html', context)


def student_dashboard(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student-dashboard.html', context)
