from rest_framework import serializers
from places.models import Place, Comment

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()
    image = serializers.ImageField()

    def validate(self,data):
        name = data.get('name')
        address = data.get('address')

        if len(name)<4:
            result = {
                "status":False,
                "message":"Name len less than 4 characters"
            }

            raise serializers.ValidationError(result)

        if address.isalpha():
            result = {
                "status": False,
                "message": "Address isalpha"
            }

            raise serializers.ValidationError(result)

        return data

    def create(self,validated_data):
        name = validated_data.get("name")
        address = validated_data.get("address")
        description = validated_data.get("description")
        image = validated_data.get("image")

        Place.objects.create(
            name=name,
            address=address,
            description=description,
            image=image
        )
        return validated_data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "place", 'comment', 'stars_given']

    def validate(self, data):
        comment = data.get('comment')
        stars_given = data.get('stars_given')


        if len(comment) < 10:
            raise serializers.ValidationError("Kommentariya 10 ta belgidan ko'p bo'lishi kerak!!!")

        if stars_given < 0 and stars_given > 5:
            raise serializers.ValidationError('Stars given minimal 1 ta maximal 5 ta bo\'lishi kerak!!!')

        return data


