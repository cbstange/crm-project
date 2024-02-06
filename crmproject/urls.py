from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import index
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
