from django.shortcuts import render
from .models import Track
from django.views.generic import TemplateView, ListView, CreateView
from .forms import TrackForm

# Create your views here.

class ListaTrackView(ListView):
    model = Track
    queryset = Track.objects.all().order_by('pub_date')

class TrackCreateView(CreateView):
    model = Track
    form_class = TrackForm
    success_url = '/tracks'   #poderia utilizar pessoa.index

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)