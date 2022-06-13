from multiprocessing import context
from django.shortcuts import render
from computerapp.models import Personnel, Machine, Infrastruture, Partenaires
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {
        'machines': machines,
        'personnels': personnels,
    }

    return render(request, 'index.html',context=context)

# Create your views here.

def machine_list_view(request):
    machines = Machine.objects.all()
    context = {'machines':machines
    }
    return render (request,'machine_list.html',context)

def perso_list_view(request):
    personnels = Personnel.objects.all()
    context = {'personnels':personnels
    }
    return render (request,'perso_list.html',context)

def infra_list_view(request):
    infra = Infrastruture.objects.all()
    context = {'infra':infra
    }
    return render (request,'infra.html',context)

def partenaires_list_view(request):
    partenaires = Partenaires.objects.all()
    context = {'partenaires': partenaires
    }
    return render (request,'partenaire.html',context)

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None )
        if form.is_valid():
            new_machine = Machine(nom = form.cleaned_data['nom'])
            new_machine.save ()
            return redirect (' machines')
    else :  
        form = AddMachineForm()
        context = {'form': form }
        return render ( request ,
        'computerapp/machine_list.html', context )
class LoginView(TemplateView):

  template_name = 'front/index.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'front/index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)