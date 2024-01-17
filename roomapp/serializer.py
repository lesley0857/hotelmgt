from .models import RoomModel,RoomfileModel
from rest_framework import serializers

class Room_list_serializer(serializers.ModelSerializer):
    files=serializers.SerializerMethodField('get_files')
    class Meta:
        model = RoomModel
        fields = ['roomname','cardNo','status','files']
    def get_files(self,obj):
        print(obj.id)
        roomfile=RoomfileModel.objects.filter(roommodel=obj.id)
        ser=Room_list_file_serializer(roomfile, many=True)
        return ser.data


                   