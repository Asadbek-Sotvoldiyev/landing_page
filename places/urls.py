from django.urls import path
from . import views

app_name = 'places'
urlpatterns = [
    path('', views.PlacesListView.as_view(),name='places'),
    path('place/<int:pk>/', views.PlaceDetail.as_view(),name='detail'),
]