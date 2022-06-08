from multiprocessing import context
from django.shortcuts import render
from computerapp.models import Personnel, Machine

def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {
        'machines': machines,
        'personnels': personnels,
    }

    return render(request, 'index.html',context=context)

# Create your views here.
