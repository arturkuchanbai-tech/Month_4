from django.urls import path
from . import views

urlpatterns = [
    path('plog_lang/', views.prog_lang_list_view),
    path('prog_lang/<int:id>/', views.prog_lang_detail_view),
    path('prog_lang/<int:id>/delete/', views.prog_lang_detail_view),
    path('prog_lang/<int:id>/update/', views.prog_lang_detail_view),


    path('create_prog_lang/', views.creste_prog_lang_view),
]

