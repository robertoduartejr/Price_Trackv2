from django.http import Http404
from django.shortcuts import render
from .models import Track
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import TrackForm

# Create views here.

class ListaTrackView(ListView):
    model = Track
    queryset = Track.objects.all().order_by('pub_date')

    def get_queryset(self): #função pra realizar o filtro
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        filtro_nome = self.request.GET.get('nome') or None
        if filtro_nome:
            queryset = queryset.filter(name__contains=filtro_nome.capitalize())

        return queryset




class TrackCreateView(CreateView):
    model = Track
    form_class = TrackForm
    success_url = '/tracks'   #poderia utilizar pessoa.index

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TrackUpdateView(UpdateView):
    model = Track
    form_class = TrackForm
    success_url = '/tracks'

class TrackDeleteView(DeleteView):
    model = Track
    success_url = '/tracks'

def chart(request, pk):
    tracks = Track.objects.filter(pk=pk)
    tracks = tracks.first()
    tracks = tracks.prices["data"]
    product = Track.objects.filter(pk=pk)
    product = product.first()
    product = product.name
    return render(request, 'track/chart.html',{'tracks': tracks, 'product': product })