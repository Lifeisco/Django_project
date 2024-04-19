"""
URL configuration for Django2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import ads as ads
from django.contrib import admin
from django.urls import path
from myapp.views import index_page, reg_page, auth_page, create_ad, log_out, view_ad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('reg/', reg_page, name='register'),
    path('auth/', auth_page, name='login'),
    path('create_ad/', create_ad, name='create_ad'),
    path('log_out/', log_out, name='log_out'),
    path('ads/', view_ad, name='ads'),
]
