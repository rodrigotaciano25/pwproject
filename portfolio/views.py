from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from portfolio.forms import NewForm

from .models import *

# Create your views here.
def index_view(request):
    return HttpResponse("Olá")

def layout_view(request):
    return render(request, 'portfolio/index.html')

def licenciatura_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)

def animacoes_view(request):
    return render(request, 'portfolio/animacoes.html')

def calculadora_view(request):
    return render(request, 'portfolio/calculadora.html')

def educacao_view(request):
    return render(request, 'portfolio/educacao.html')

def hobbies_view(request):
    return render(request, 'portfolio/hobbies.html')

def skills_view(request):
    return render(request, 'portfolio/skills.html')

def website_view(request):
    return render(request, 'portfolio/website.html')

def blog_view(request):
    context = {'news': New.objects.all()}
    return render(request, 'portfolio/blog.html', context)

def nova_tarefa_view(request):
    form = NewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'form': form}
    return render(request, 'portfolio/blog_novo.html', context)

@login_required
def edita_tarefa_view(request, portfolio_id):
    tarefa = New.objects.get(id=portfolio_id)
    form = NewForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'form': form, 'portfolio_id': portfolio_id}
    return render(request, 'portfolio/blog_editar.html', context)

def apaga_tarefa_view(request, portfolio_id):
    New.objects.get(id=portfolio_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

def login_view(request):
    if request.method == "POST":
        nome_login = request.POST.get('username')
        password_login = request.POST.get('password')
        utilizador = authenticate(request, username=nome_login, password=password_login)

        if utilizador is not None:
            login(request, utilizador)
            context = {'post': New.objects.all(),}
            return render(request, 'portfolio/index.html', context)
        else:
            return render(
                request, 'portfolio/login.html',
                {'message': "Credenciais Invalidas"}
            )

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'portfolio/index.html')

def contactos_view(request):
    return render(request, 'portfolio/contactos.html')


def labs_view(request):
    context = {'labs': Lab.objects.all()}
    return render(request, 'portfolio/labs.html', context)