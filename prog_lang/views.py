from django.shortcuts import render, get_list_or_404
from . import models

def prog_lang_detail_view(request, id):
    if request.method == 'GET':
        prog_lang_id = models.Proglang.objects.filter(id=id)
        return render(
            request,
            'prog_lang_detdil.html',
            context={
                'prog_id_input': prog_lang_id
            }
        )


def prog_lang_list_view(request):
    if request.method == 'GET':
        prog_lang = models.Proglang.objects.all()
        return render(
            request,
            'prog_languages.html',
            {
                'prog_lang': prog_lang
            }
        )