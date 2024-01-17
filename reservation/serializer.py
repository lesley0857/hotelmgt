from .models import ReservationModel, ReservedRooms
from rest_framework import serializers

class Reservation_list_serializer(serializers.ModelSerializer):
    reservedroom=serializers.SerializerMethodField('get_files')
    user=serializers.StringRelatedField()
    preference=serializers.StringRelatedField()
    class Meta:
        model = ReservationModel
        fields = ['user','checkInDateandTime','preference','reservedroom']
    def get_reservedroom(self,obj):
        print(obj.id)
        reserved_rooms=ReservedRooms.objects.filter(reservedroom=obj.id)
        serialized_reserved_rooms=Reservation_list_serializer(reserved_rooms, many=True)
        return serialized_reserved_rooms.data