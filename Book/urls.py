from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.my_book_view),
    path('main/', views.main),
    path('photo/', views.photo),
    path('books/', views.BoookListView.as_view(), name='book_list'),
    path('books/create/', views.CreateBookView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', views.UpdateBookView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', views.DeleteBookView.as_view(), name='book_delete'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', views.SearchView.as_view(), name='book_search'),
]




