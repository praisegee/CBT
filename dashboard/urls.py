from django.urls import path, include

# from dashboard.views import admin_dashboard

app_name = 'dashboard'

urlpatterns = [
	path('student/', include('dashboard.urls_manager.student_urls', 'student')),
	path('lecturer/', include('dashboard.urls_manager.lecturer_urls', 'lecturer')),
	# path('admin/', admin_dashboard, name="admin-dashboard"),
]