from django.urls import path
from . import views

<<<<<<< HEAD
app_name='yaziki'
urlpatterns = [
    path('prog_lang/', views.ProgLangListView.as_view(), name='yaizki_programmirovanie'),
    path('prog_lang/<int:id>/', views.ProgLangDetailView.as_view()),
    path('prog_lang/<int:id>/delete/', views.DeleteProgLangView.as_view()),
    path('prog_lang/<int:id>/update/', views.UpdateProgLangView.as_view()),
    path('create_prog_lang/', views.CreateProgLangView.as_view(), name='sozdat_blog'),


    path('prog_lang/search/', views.SearchView.as_view(), name='search_prog_lang')]
=======
app_name = 'yaziki'

urlpatterns = [
    path('prog_lang/', views.prog_lang_list_view),
    path('prog_lang/<int:id>/', views.prog_lang_detail_view),
    path('prog_lang/<int:id>/delete/', views.delete_prog_lang_view),

    # CBV обязательно с .as_view()
    path('prog_lang/<int:id>/update/', views.Update.as_view()),
    path('search/', views.Search.as_view()),

    path('create_prog_lang/', views.create_prog_lang_view, name='sozdat_blog'),
]
>>>>>>> 88e1fbe6 (Классные работы)
