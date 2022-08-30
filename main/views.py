from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from .forms import NovoUsuarioForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from .models import CustomUser

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/base.html'


class UserCreateView(CreateView):  #utilizei essa classe ao inves do metodo register do video
    model = CustomUser
    form_class = NovoUsuarioForm
    success_url = '/'   #poderia utilizar pessoa.index

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

