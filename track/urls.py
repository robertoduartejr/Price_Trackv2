from django.urls import path
from .views import ListaTrackView,TrackCreateView, TrackUpdateView, TrackDeleteView, chart
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required( ListaTrackView.as_view()),name='track.index'),
    path('novo/', login_required( TrackCreateView.as_view()),name='track.novo'),
    path('editar/<int:pk>', login_required( TrackUpdateView.as_view()),name='track.editar'),
    path('remover/<int:pk>', login_required( TrackDeleteView.as_view()),name='track.remover'),
    path('chart/<int:pk>', login_required(views.chart),name='track.chart'),


]