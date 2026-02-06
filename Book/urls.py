from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.my_book_view),
    path('main/', views.main),
    path('photo/', views.photo),
    
]


