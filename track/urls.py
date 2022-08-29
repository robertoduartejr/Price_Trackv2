from django.urls import path
from .views import ListaTrackView,TrackCreateView


urlpatterns = [
    path('', ListaTrackView.as_view(),name='track.index'),
    path('novo/', TrackCreateView.as_view(),name='track.novo')

]