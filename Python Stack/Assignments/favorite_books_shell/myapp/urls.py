from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books, name='books'),
    path('users', views.users, name='users'),
    path('favorite_books', views.favorite_books, name='favorite_books'),
]