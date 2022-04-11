from django.contrib import admin

from tests.models import Question, Notification

admin.site.register(Question)
admin.site.register(Notification)
