from rest_framework import serializers

from .models import Customer

from ..users.serializer import UserSerializer
from ..picture.serializer import PictureSerializer
from ..announcement.serializer import AnnouncementSerializer
from ..productor.serializer import ProductorSerializer

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    idPicture = PictureSerializer(many=False, read_only=True)
    idAnunFav = AnnouncementSerializer(many=True, read_only=True)
    idProdFav = ProductorSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['user', 'idPicture', 'idAnunFav', 'idProdFav']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        return Customer.objects.create(user=user, **validated_data)
