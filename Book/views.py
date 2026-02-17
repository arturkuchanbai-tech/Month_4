
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponse
from .forms import BookForm
from django.core.paginator import Paginator
from decouple import config

def book_list(request):
    # Получаем строку поиска из GET-параметров
    query = request.GET.get('q', '')

    # Проверяем флаг скрытия секретных книг из .env
    hide_secret = config('HIDE_SECRET', default=False, cast=bool)

    # Фильтруем книги по поиску и секретности
    books = Book.objects.all()
    if hide_secret:
        books = books.filter(secret=False)  # поле secret должно быть в модели Book
    if query:
        books = books.filter(title__icontains=query)

    # Пагинация — 10 книг на страницу
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books.html', {'page_obj': page_obj, 'query': query})


def book_list(request):
    books = Book.objects.all()
    return render(
        request,
        "book/book_list.html",
        {"books": books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(
        request,
          "book/book_form.html",
            {"form": form})

def book_update(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(
        request,
          "book/book_form.html",
            {"form": form})

def book_delete(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(
        request,
          "book/book_delete.html",
            {"book": book})


def my_book_view(request):
    if request.method == 'GET':
        return HttpResponse('Жизнь — это то, что с тобой происходит, пока ты строишь планы.Автор: Джон Леннон ')


def main(request):
    if request.method == 'GET':
        return HttpResponse('<strong>Artur Backend Developer')
    

def photo(request):
    if request.method == 'GET':
        return HttpResponse(978-5-389-14702-'<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" width="400">')


def book_list(request):
    books = Book.objects.all()
    return render(
        request,
          'book/book_list.html',
            {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(
        request,
          'book/book_detail.html',
            {'book': book})
