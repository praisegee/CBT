from django.urls import path

from dashboard.views_manager.lecturer_view_manager import (
		questions,
		show_result,
		attendance,
		download_result,
	)

app_name = 'dashboard'

urlpatterns = [
	path('questions/', questions, name="questions"),
	path('show_result/', show_result, name="show-result"),
	path('attendance/', attendance, name="attendance"),
	path('download_result/', download_result, name="download-result"),
]