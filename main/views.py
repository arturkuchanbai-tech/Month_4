from django.views.generic import (CreateView,UpdateView,DeleteView,DetailView,ListView)
from django.urls import reverse_lazy
from .models import Proglang
from .forms import ProgLangForm



class ProgLangListView(ListView):
    model = Proglang
    template_name = 'prog_lang_list.html'
    context_object_name = 'prog_langs'



class ProgLangCreateView(CreateView):
    model = Proglang
    form_class = ProgLangForm
    template_name = 'create_prog_lang.html'
    success_url = reverse_lazy('prog_lang_list')



class ProgLangDetailView(DetailView):
    model = Proglang
    template_name = 'prog_lang_detail.html'
    context_object_name = 'prog_lang'



class ProgLangUpdateView(UpdateView):
    model = Proglang
    form_class = ProgLangForm
    template_name = 'update_prog_lang.html'
    success_url = reverse_lazy('prog_lang_list')



class ProgLangDeleteView(DeleteView):
    model = Proglang
    template_name = 'prog_lang_confirm_delete.html'
    success_url = reverse_lazy('prog_lang_list')
