from django.urls import path
from . import views

urlpatterns = [
    path('plog_lang/', views.prog_lang_list_view),
    path('prog_lang/<int:id>/', views.prog_lang_detail_view),
]

