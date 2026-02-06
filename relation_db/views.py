from django.shortcuts import render
from . import models

def relation_db(request):
    if request.method == 'GET':
        persons_tour = models.Register.objects.all()
    return render(
        request,
        'relation_db.html',
        {
            'number_car': persons_tour
        }
    )
    