from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import New

# Create your views here.
def index_view(request):
    return HttpResponse("Olá")

def layout_view(request):
    return render(request, 'portfolio/index.html')

def licenciatura_view(request):
    return render(request, 'portfolio/licenciatura.html')

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
    return render(request, 'portfolio/blog.html')

def blog_novo_view(request):
    return render(request, 'portfolio/blog_novo.html')

def blog_editar_view(request):
    return render(request, 'portfolio/blog_editar.html')

def login_view(request):
    if request.method == "POST":
        nome_login = request.POST.get('username')
        password_login = request.POST.get('password')
        utilizador = authenticate(request, username=nome_login, password=password_login)

        if utilizador is not None:
            login(request, utilizador)
            context = {'post': New.objects.all(),}
            return render(request, 'portfolio/blog.html', context)
        else:
            return render(
                request, 'portfolio/login.html',
                {'message': "Credenciais Invalidas"}
            )

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'portfolio/home.html')