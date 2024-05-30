from django.shortcuts import render

from quiz.models import Dato

def datos (request):
    personales=Dato.objects.all()
    return render(request, "index.html", {'datos':personales,})
