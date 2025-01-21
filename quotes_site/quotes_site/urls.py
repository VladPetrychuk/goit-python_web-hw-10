"""
URL configuration for quotes_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Вхід користувача
    path('login/', LoginView.as_view(template_name='quotes/login.html'), name='login'),
    # Вихід користувача
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('authors/', views.authors_list, name='authors_list'),  # Список авторів
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),  # Деталі автора
    path('quotes/', views.quotes_list, name='quotes_list'),  # Список цитат
]