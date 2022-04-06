from django.urls import path
from dashboard.views_manager.student_view_manager import (
		tests_view,
		check_result,
		print_result,
		write_test, 
	)

app_name = 'dashboard'

urlpatterns = [
	path('test/', tests_view, name="tests"),
	path('result/', check_result, name="result"),
	path('print_result/', print_result, name="print-result"),
	path('write_test/<int:pk>/', write_test, name="write-test"),
]