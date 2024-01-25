from .models import PaymentModel
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentModel
        fields='__all__'