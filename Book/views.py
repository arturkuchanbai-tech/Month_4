from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Book

def my_book_view(request):
    if request.method == 'GET':
        return HttpResponse('Жизнь — это то, что с тобой происходит, пока ты строишь планы.Автор: Джон Леннон ')


def main(request):
    if request.method == 'GET':
        return HttpResponse('<strong>Artur Backend Developer')
    
def photo(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" width="400">')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_list_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})
