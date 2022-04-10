
import csv, json #, openpyxl

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tests.models import Question


@login_required
def tests_view(request, *args, **kwargs):
	questions 	= Question.objects.all().order_by('-date_created')
	context 	= {'questions':questions}
	return render(request, 'dashboard/student_templates/tests.html', context)



@login_required
def write_test(request, pk, *args, **kwargs):
	question 	= Question.objects.get(id=pk)
	context 	= {'question':question}
	return render(request, 'dashboard/student_templates/write-test.html', context)



@login_required
def check_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/check-result.html', context)

@login_required
def print_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/print-result.html', context)