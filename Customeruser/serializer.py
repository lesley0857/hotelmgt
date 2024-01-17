from .models import *
from rest_framework import serializers


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomBaseuser
        fields = ['firstname', 'lastname', 'birth_date', 'email',
                  'phone_number',
                  'profile_pic', 'password',]
       # extra_kwargs = {'password',{'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance