from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, View
from .models import Place, Comment
from .forms import AddCommentForm


class PlacesListView(View):
    def get(self, request):
        places = Place.objects.all()
        search_query = request.GET.get('q', '')
        if search_query:
            places = Place.objects.filter(name__icontains=search_query)
        return render(request, 'places/places.html', {"places": places, 'search_query': search_query})


class PlaceDetail(View):
    def get(self, request, pk):
        form = AddCommentForm()
        place = Place.objects.get(id=pk)

        return render(request, 'places/detail.html', {'place': place, 'form':form})


class AddCommentView(LoginRequiredMixin,View):
    def post(self, request, pk):
        form = AddCommentForm(request.POST)
        place = Place.objects.get(id=pk)
        if form.is_valid():
            place = Place.objects.get(id=pk)
            Comment.objects.create(
                user=request.user,
                place=place,
                comment=form.cleaned_data['comment'],
                stars_given=form.cleaned_data['stars_given'],
            )
            return redirect(reverse('places:detail', kwargs={'pk': place.id}))
        return render(request, 'places/detail.html', {'place': place, 'form': form})
