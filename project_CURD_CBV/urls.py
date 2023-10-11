"""
URL configuration for project_CURD_CBV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,re_path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',TemplateView.as_view(template_name='app/Home.html'),name='Home'),
    path('SchoolList/',SchoolList.as_view(),name='SchoolList'),
    path('SchoolCreate/',SchoolCreate.as_view(),name='SchoolCreate'),
    path('StudentCreate/',StudentCreate.as_view(),name='StudentCreate'),


    re_path('(?P<pk>\d+)/',SchoolDetails.as_view(), name='SchoolDetails'),
    re_path('(?P<pk>\d+)/',StudentDetails.as_view(),name='StudentDetails'),
]
