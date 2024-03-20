from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from places.models import Place


class PlacesListView(ListView):
    model = Place
    context_object_name = 'places'
    template_name = 'places/places.html'

class PlaceDetail(DetailView):
    model = Place
    context_object_name = 'place'
    template_name = 'places/detail.html'


