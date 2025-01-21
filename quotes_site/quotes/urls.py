from django.urls import path
from . import views  # Імпортуємо ваші в'юхи

urlpatterns = [
    path('', views.index, name='index'),  # Головна сторінка
    path('authors/', views.authors_list, name='authors_list'),  # Список авторів
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),  # Деталі автора
    path('quotes/', views.quotes_list, name='quotes_list'),  # Список цитат
]