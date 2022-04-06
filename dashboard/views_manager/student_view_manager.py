from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from tests.models import Question

import pandas as pd



def df_convert(data):

	test = {}

	if data.endswith('.csv'):
		data_frame = pd.read_csv(data)
	elif data.endswith('.xlsx'):
		data_frame = pd.read_excel(data)
	elif data.endswith('.json'):
		data_frame = pd.read_csf(data)
	else:
		return None

	py_dict_data = data_frame.to_dict()

	for column in py_dict_data:
		test[column] = [value for value in py_dict_data[column].values()]
	
	return test




@login_required
def tests_view(request, *args, **kwargs):
	questions 	= Question.objects.all().order_by('-date_created')
	context 	= {'questions':questions}
	return render(request, 'dashboard/student_templates/tests.html', context)



@login_required
def write_test(request, pk, *args, **kwargs):
	question 	= Question.objects.get(id=pk)
	test 		= df_convert(f'.{question.file.url}')
	length 		= [range(len(test['question']))]
	context 	= {'question':question, 'test':test}
	print(test)
	return render(request, 'dashboard/student_templates/write-test.html', context)



@login_required
def check_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/check-result.html', context)

@login_required
def print_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/student_templates/print-result.html', context)