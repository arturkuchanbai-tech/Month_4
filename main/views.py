from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms

def update(request,id):
    prog_lang = get_object_or_404(models.Proglang, id= id)
    if request.method == "POST":
        form = forms.ProgLangForm(request.POST, instance=prog_lang)
        if form.is_valid():
            form.save()
            return redirect('/prog_lang/')
    else:
        form = forms.ProgLangForm(instance=prog_lang)
    return render(
        request,
        'update_prog_lang.html',
        {
            'form': form,
            'prog_lang': prog_lang
        }
    )




def delate(request,id):
    prog_lang = get_object_or_404(models.Proglang, id =id)
    prog_lang.delate
    return redirect('/plog_lang/')


#create prog lang
def creste_prog_lang_view(request):
    if request.method == 'POST':
        form = forms.ProgLangForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/plog_lang/')
    else:
        form = forms.ProgLangForm()

    return render(
        request,
        "create_prog_lang.html",
        {
            "form":form
        }
    )





#read
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

