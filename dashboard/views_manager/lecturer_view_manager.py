from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tests.forms import QuestionForm
from tests.models import Question

@login_required
def questions(request, *args, **kwargs):

	context 		= {}
	question_form 	= QuestionForm(request.POST or None, request.FILES or None)
	questions 		= Question.objects.all().order_by('-date_created')

	context['question_form'] 	= question_form
	context['questions'] 		= questions

	if question_form.is_valid():

		course_title 		= question_form.cleaned_data.get('course_title')
		course_code 		= question_form.cleaned_data.get('course_code')
		instruction 		= question_form.cleaned_data.get('instruction')
		no_of_question 		= question_form.cleaned_data.get('no_of_question')
		minite_to_finish 	= question_form.cleaned_data.get('minite_to_finish')
		test_date		 	= question_form.cleaned_data.get('test_date')
		file 				= question_form.cleaned_data.get('file')

		question 				= Question(
									lecturer=request.user.lecturer,
									course_title=course_title,
									course_code=course_code,
									instruction=instruction,
									no_of_question=no_of_question,
									minite_to_finish=minite_to_finish,
									test_date=test_date,
									file=file
								)
		question.save()

		return redirect('dashboard:lecturer:questions')

	return render(request, 'dashboard/lecturer_templates/questions.html', context)


@login_required
def show_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/lecturer_templates/show-result.html', context)


@login_required
def attendance(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/lecturer_templates/attendance.html', context)


@login_required
def download_result(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/lecturer_templates/download-result.html', context)
