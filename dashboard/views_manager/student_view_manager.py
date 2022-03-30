from django.shortcuts import render

def tests_view(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/tests.html', context)

def check_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/check-result.html', context)

def print_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/print-result.html', context)