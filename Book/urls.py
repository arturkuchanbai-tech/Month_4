from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.my_book_view),
]


