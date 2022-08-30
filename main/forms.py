from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True) #tornar email como obrigatorio e único

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True): #redefiniu o metodo save pq quero fazer algo a mais que simplesmente salvar
        user = super(NovoUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
