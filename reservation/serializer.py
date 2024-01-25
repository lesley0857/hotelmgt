from .models import ReservationModel, ReservedRooms
from Payment.serializers import PaymentSerializer
from Payment.models import PaymentModel
from rest_framework import serializers

class ReservedRoomsSerializer(serializers.ModelSerializer):
    room=serializers.StringRelatedField()
    class Meta:
        model=ReservedRooms
        fields='__all__'

class Reservation_list_serializer(serializers.ModelSerializer):
    reservedroom=serializers.SerializerMethodField('get_reservedroom')
    user=serializers.StringRelatedField()
    preference=serializers.StringRelatedField()
    payment=serializers.StringRelatedField()
    class Meta:
        model = ReservationModel
        fields = ['user','checkInDateandTime','preference','reservedroom','payment']
    def get_reservedroom(self,obj):
        print(obj)
        reserved_rooms=ReservedRooms.objects.filter(reservedroom=obj)
        serialized_reserved_rooms=ReservedRoomsSerializer(reserved_rooms, many=True)
        return serialized_reserved_rooms.data
    