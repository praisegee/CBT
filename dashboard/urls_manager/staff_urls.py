from django.urls import path

from dashboard.views_manager.student_view_manager import (
		tests_view,
	)

app_name = 'dashboard'

urlpatterns = [
	path('', tests_view, name="tests")
]