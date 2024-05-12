from django.core.paginator import Paginator
from django.shortcuts import render

from models_list_displaying.books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 10)
    page_date = request.GET.get('date')
    page = paginator.get_page(page_date)

    context = {
        'books': books_list,
        'page': page,
    }

    return render(request, template, context)
