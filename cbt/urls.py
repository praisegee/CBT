
# MAIN URL ROUTES

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('account.urls', 'account')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls', 'dashboard'))
]
