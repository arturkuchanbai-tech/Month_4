from django.shortcuts import render, get_object_or_404,redirect
from . import models, forms
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic




#search
class SearchView(generic.ListView):
    template_name = 'prog_lang/prog_languages.html'
    context_object_name = 'prog_lang'
    model = models.ProgLang

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s']= self.request.GET.get('s')
        return context







#UPDATE
class UpdateProgLangView(generic.UpdateView):
    template_name = 'prog_lang/update_prog_lang.html'
    form_class = forms.ProgLangForm
    model = models.ProgLang
    success_url = '/prog_lang/'

    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)
    
    def form_valid(self, form):
        print(form.changed_data)
        return super(UpdateProgLangView, self).form_valid(form=form)
    
        





#DELETE PROG LANG
class DeleteProgLangView(generic.DeleteView):
    template_name = 'prog_lang/confirm_delete.html'
    success_url = '/prog_lang/'
    context_object_name = 'prog_lang_id'
    model = models.ProgLang

    def get_object(self, **kwargs):
        prog_lang_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=prog_lang_id)






#CREATE PROG LANG
class CreateProgLangView(generic.CreateView):
    template_name = 'prog_lang/create_prog_lang.html'
    form_class = forms.ProgLangForm
    success_url = '/prog_lang/'


    def form_valid(self, form):
        print(form.changed_data)
        return super(CreateProgLangView, self).form_valid(form=form)







#READ

class ProgLangDetailView(generic.DetailView):
    template_name = 'prog_lang/prog_lang_detail.html'
    context_object_name = 'prog_id'
    pk_url_kwarg = 'id'
    model = models.ProgLang

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request

        #Проверяем кол-во просмотров
        views_lang = request.session.get('viewed_lang', [])

        if obj.pk not in views_lang:
            models.ProgLang.objects.filter(pk=obj.pk).update(
                views = F("views")+1
            )
            views_lang.append(obj.pk)
            request.session['viewed_lang'] = views_lang

            #Обновить после изменения
            obj.refresh_from_db()
        return obj



#list 
class ProgLangListView(generic.ListView):
    template_name = 'prog_lang/prog_languages.html'
    model = models.ProgLang
    context_object_name = 'prog_lang'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем prog_lang как псевдоним для page_obj
        context['prog_lang'] = context['page_obj']
        return context

   