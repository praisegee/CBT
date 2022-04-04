from django.contrib import admin

from roles.models import Lecturer, Student


admin.site.register(Lecturer)
admin.site.register(Student)
