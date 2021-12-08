"""movie_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from movie_app.views import get_movie_list, add_movie, edit_movie, toggle_movie
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_movie_list, name='get_movie_list'),
    path('add/', views.add_movie, name='add'),
    path('edit/<movie_id>', views.edit_movie, name='edit'),
    path('toggle/<movie_id>', views.toggle_movie, name='toggle'),
    path('delete/<movie_id>', views.delete_movie, name='delete'),
]