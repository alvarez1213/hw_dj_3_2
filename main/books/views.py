from django.shortcuts import render, redirect, get_list_or_404
from .models import Book


def index(request):
    return redirect('books')

def books_view(request):
    context = Book.objects.all()
    template = 'books/books_list.html'
    return render(request, template, {'books': context, 'pagination': False})

def books_view_filter(request, pub_date):
    context = get_list_or_404(Book, pub_date=pub_date)
    template = 'books/books_list.html'
    date_less, date_next = None, None

    date_has_previous = Book.objects.filter(pub_date__lt=pub_date).values('pub_date').first()
    if date_has_previous:
        date_less = date_has_previous.get('pub_date').strftime('%Y-%m-%d')

    date_has_next = Book.objects.filter(pub_date__gt=pub_date).values('pub_date').first()
    if date_has_next:
        date_next = date_has_next.get('pub_date').strftime('%Y-%m-%d')

    return render(request, template, {'books': context,
                                      'pagination': True,
                                      'date_less': date_less,
                                      'date_next': date_next})