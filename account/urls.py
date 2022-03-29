from django.urls import path

from account.views import (
        login_view,
        staff_register_view,
        student_register_view,
        logout_view,
    )

app_name = "account"

urlpatterns = [
    path('', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('staff-register/', staff_register_view, name="staff-register"),
    path('student-register/', student_register_view, name="student-register"),
]
