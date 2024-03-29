"""p32 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Registration/',Registration,name='Registration'),
    path('home/',home,name='home'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('dp/', dp, name = 'dp'),
    path('change_password/',change_password,name='change_password'),
    path('forget_password/',forget_password,name='forget_password'),
    path('match_otp/',match_otp,name='match_otp'),
    path('fp/',fp,name='fp'),
    path('change_profile/',change_profile,name='change_profile'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
