from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def tests_view(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/tests.html', context)

@login_required
def check_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/check-result.html', context)

@login_required
def print_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/print-result.html', context)