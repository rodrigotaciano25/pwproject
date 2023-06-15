"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.layout_view, name='index'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('educacao/', views.educacao_view, name='educacao'),
    path('animacoes/', views.animacoes_view, name='animacoes'),
    path('calculadora/', views.calculadora_view, name='calculadora'),
    path('hobbies/', views.hobbies_view, name='hobbies'),
    path('skills/', views.skills_view, name='skills'),
    path('website/', views.website_view, name='website'),
    path('blog', views.blog_view, name='blog'),
    path('blog_novo/', views.nova_tarefa_view, name='blog_novo'),
    path('blog_editar/<int:portfolio_id>', views.edita_tarefa_view, name='blog_editar'),
    path('apaga/<int:portfolio_id>', views.apaga_tarefa_view, name='apaga'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('contactos/', views.contactos_view, name='contactos'),
    path('labs/', views.labs_view, name='labs'),
]
