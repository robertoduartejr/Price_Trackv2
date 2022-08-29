from django import forms
from .models import Track


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['name','url','site','desired_price','ativa']
        #poderia ser fields = ['__all__'] dessa forma viria todos
