<<<<<<< HEAD
from django.views.generic import ListView
from .models import Register

class RelationDBView(ListView):
    model = Register                       
    template_name = 'relation_db.html'  
    context_object_name = 'number_car'     

=======
from django.shortcuts import render

from django.shortcuts import render
from . import models


def relation_db(request):
    if request.method == 'GET':
        nummer_car = models.NumberCar.objects.all()    
    return render(
        request, 
        'relation_db.html',
        {
            'nummer_car': nummer_car
        }
    )
>>>>>>> 88e1fbe6 (Классные работы)
