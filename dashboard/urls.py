from django.urls import path

from dashboard.views import user_dashboard, admin_dashboard

app_name = 'dashboard'

urlpatterns = [
	path('', user_dashboard, name="dashboard"),
	path('admin/', admin_dashboard, name="admin-dashboard"),
]