from .serializers import PlaceSerializer,CommentSerializer
from places.models import Place, Comment
from rest_framework.views import APIView
from rest_framework.response import Response

class PlaceApiView(APIView):
    def get(self, request):
        place = Place.objects.all()
        serializer = PlaceSerializer(place, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"result": "success"})

class PlaceDetailApiView(APIView):
    def get(self, request, id):
        place = Place.objects.get(id=id)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

class CommentListApiView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Result":"Success"})