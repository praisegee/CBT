import json, csv
from django.shortcuts import render
from django.http import JsonResponse


from tests.models import Question



def get_question(request, pk, *args, **kwargs):

	question 	= Question.objects.get(id=pk)
	file_path	= f'.{question.file.url}'

	test = []
	data = []
	new = {}

	with open(file_path, 'r') as f:
		file = csv.reader(f)

		for csv_row in file:
			test.append(csv_row)

		for index,row in enumerate(test):
			new["question"] = test[index][0]
			new["optionA"] 	= test[index][1]
			new["optionB"] 	= test[index][2]
			new["optionC"] 	= test[index][3]
			new["optionD"] 	= test[index][4]
			new["answer"] 	= test[index][5]
			data.append(new.copy())

		return JsonResponse(data, safe=False)

