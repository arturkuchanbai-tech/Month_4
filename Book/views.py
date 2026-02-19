from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm
from django.views import generic
from django.db.models import F

class SearchView(generic.ListView):
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s']= self.request.GET.get('s')
        return context


class BoookListView(generic.ListView):
    template_name = 'book/book_list.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['books_page'] = context['page_obj']
        return context

class CreateBookView(generic.CreateView):
    template_name = 'book/book_form.html'
    form_class = BookForm
    success_url = '/book/'


    def form_valid(self, form):
        print(form.changed_data)
        return super(CreateBookView, self).form_valid(form=form)

#UPDATE
class UpdateBookView(generic.UpdateView):
    template_name = 'book/book_form.html'
    form_class = BookForm
    model = Book
    success_url = '/book/'

    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)
    
    def form_valid(self, form):
        print(form.changed_data)
        return super(UpdateBookView, self).form_valid(form=form)
    

class DeleteBookView(generic.DeleteView):
    template_name = 'book/confirm_delete.html'
    success_url = '/book/'
    context_object_name = 'book'
    model = Book

    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)

def my_book_view(request):
    if request.method == 'GET':
        return HttpResponse('Жизнь — это то, что с тобой происходит, пока ты строишь планы.Автор: Джон Леннон ')


def main(request):
    if request.method == 'GET':
        return HttpResponse('<strong>Artur Backend Developer')
    

def photo(request):
    if request.method == 'GET':
        return HttpResponse(978-5-389-14702-'<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" width="400">')



class BookDetailView(generic.DetailView):
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'
    model = Book

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request

        
        viewed_books = request.session.get('viewed_book', [])

        if obj.pk not in viewed_books:
            Book.objects.filter(pk=obj.pk).update(
                views = F("views")+1
            )
            viewed_books.append(obj.pk)
            request.session['viewed_lang'] = viewed_books

            
            obj.refresh_from_db()
        return obj
