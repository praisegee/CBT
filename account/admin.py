from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User

from account.forms import AdminRegistrationForm


class AdminUser(UserAdmin):
	list_display = ('username', 'email', 'last_login', 'is_admin', 'is_lecturer', 'is_student')
	readonly_fields = ('last_login', 'date_joined')
	search_fields = ('username', 'email')
	exclude = ('password1', 'password2')

	add_form = AdminRegistrationForm

	list_filter = ()
	fieldsets = ()


admin.site.register(User, AdminUser)


