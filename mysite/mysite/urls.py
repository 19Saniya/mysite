"""
URL configuration for mysite project.

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bootstrap, name="home"),
    path('triangle/', views.triangle),
    path('userform/', views.userform, name="userform"),
    path('about/', views.about, name="about"),
    path('course/', views.course),
    path('course/<courseid>', views.coursedetails),
    # path('saveuser/', views.saveuser, name="saveuser")
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
]
