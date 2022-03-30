from django.shortcuts import render

from dashboard.views_manager.student_view_manager import (
		tests_view,
	)

def admin_dashboard(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/admin-dashboard.html', context)


def student_dashboard(request, *args, **kwargs):
	return tests_view(request)
