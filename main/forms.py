from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'name@example.com'})) #tornar email como obrigatorio e único
    password1 = forms.CharField(widget=forms.PasswordInput(   #needed to declare here in order to use bootstrap
        attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}, ))
    password2 = forms.CharField(widget=forms.PasswordInput(    #needed to declare here in order to use bootstrap
        attrs={'class': 'form-control', 'placeholder': 'Confirm password', 'required': 'required'}, ))

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Define your unique username'}),
            #'email': forms.EmailInput(attrs={'class': 'form-control'}),
            #'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            #'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

            #o único que dava pra fazer no widgets era o username, porque o email eu tive que colocar como requerido e teve mudança
            #e o password a unica forma de fazer é pelo init ou pela forma que fiz acima
        }

    def save(self, commit=True): #redefiniu o metodo save pq quero fazer algo a mais que simplesmente salvar
        user = super(NovoUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit: #trabalhar aqui com a ideia de mandar o email
            user.save()
        return user

