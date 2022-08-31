from django import forms
from .models import Track


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name','url','site','desired_price','ativa']
        #poderia ser fields = ['__all__'] dessa forma viria todos

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Define your track name'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.example.com'}),
            'site': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose Site'}),
            'desired_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Define your unique username'}),
            'ativa': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Define your unique username'}),

            # o único que dava pra fazer no widgets era o username, porque o email eu tive que colocar como requerido e teve mudança
            # e o password a unica forma de fazer é pelo init ou pela forma que fiz acima
        }