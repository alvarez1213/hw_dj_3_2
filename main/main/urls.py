from django.contrib import admin
from django.urls import path
from books.views import books_view, books_view_filter, index


urlpatterns = [
    path('', index),
    path('books', books_view, name='books'),
    path('books/<pub_date>/', books_view_filter, name='books'),
    path('admin/', admin.site.urls),
]