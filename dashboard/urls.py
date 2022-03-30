from django.urls import path, include

from dashboard.views import admin_dashboard

app_name = 'dashboard'

urlpatterns = [
	path('student/', include('dashboard.urls_manager.student_urls', 'student')),
	path('staff/', include('dashboard.urls_manager.staff_urls', 'staff')),
	path('admin/', admin_dashboard, name="admin-dashboard"),
]