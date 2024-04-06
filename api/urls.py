from django.urls import path
from .views import PlaceApiView, PlaceDetailApiView, CommentListApiView

urlpatterns = [
    path('places/', PlaceApiView.as_view()),
    path('detail/<int:id>/', PlaceDetailApiView.as_view()),
    path('comments/', CommentListApiView.as_view()),
]