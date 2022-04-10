from django.urls import path

from api.views import (
		get_question,
	)

urlpatterns = [
	path('question/<str:pk>/', get_question, name="question"),
]