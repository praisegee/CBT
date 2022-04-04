from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from dashboard.views_manager.student_view_manager import (
		tests_view,
	)


@login_required
def admin_dashboard(request, *args, **kwargs):
	context = {}
	return render(request, 'dashboard/admin-dashboard.html', context)

@login_required
def student_dashboard(request, *args, **kwargs):
	return tests_view(request)
