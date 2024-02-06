from django.contrib import admin
from django.urls import path
from core.views import index
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('sign-up/', signup, name='signup'),
    path('admin/', admin.site.urls),
]
