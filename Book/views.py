from django.shortcuts import render
from django.http import HttpResponse

def my_book_view(request):
    if request.method == 'GET':
        return HttpResponse('Жизнь — это то, что с тобой происходит, пока ты строишь планы.Автор: Джон Леннон ')


