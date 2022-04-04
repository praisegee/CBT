
# MAIN URL ROUTES

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import (
        PasswordResetView,
        PasswordResetDoneView,
        PasswordResetConfirmView,
        PasswordResetCompleteView,
    )

urlpatterns = [
    path('', include('account.urls', 'account')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls', 'dashboard')),


    path('reset_password/', 
        PasswordResetView.as_view(template_name="account/password-reset.html"), 
        name="password_reset"),

    path('reset_password_sent/', 
        PasswordResetDoneView.as_view(template_name="account/password-reset-sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(template_name="account/password-reset-confirm.html"), 
        name="password_reset_confirm"),

    path('reset-password_complete/', 
        PasswordResetCompleteView.as_view(template_name="account/password-reset-complete.html"), 
        name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
