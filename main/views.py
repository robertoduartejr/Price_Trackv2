from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .forms import NovoUsuarioForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from .models import CustomUser
from django.core.mail import send_mail
from backendfunctions import send_email_confirmation

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/base.html'

def register(request):
    if request.method == "POST":
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            #if user != None: @ it's a way to check if I saved or not
            login(request, user)
            messages.success(request, "Seja bem-vindo ao Track Price. Em breve receberá um email com a confirmação do cadastro!")
            send_email_confirmation(form)
            return redirect('home')
        messages.error(request, "Falha no cadastro do usuário.")
    form = NovoUsuarioForm()
    context = {'form': form}
    return render(request, template_name='main/register.html', context=context)


#tudo abaixo não esta sendo utilizado, mas é uma forma de resolver
class UserCreateView(CreateView):  #utilizei essa classe ao inves do metodo register do video
    model = CustomUser
    form_class = NovoUsuarioForm
    success_url = '/'   #poderia utilizar pessoa.index

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


