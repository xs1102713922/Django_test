"""
URL configuration for test project.

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
from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/2003',views.page_2003_view),
    #path('print/<int:num1>/<str:op>/<int:num2>',views.print_view),
    re_path(r'birthday/(?P<year>\d{1,4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$',views.birthday_view),
    re_path(r'birthday/(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{1,4})$',views.birthday_view),
    path('test_request',views.test_request),
    path('post_test',views.post_test)
]
