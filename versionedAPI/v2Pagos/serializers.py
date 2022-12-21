from rest_framework import serializers
from pagos.models import Pagos

class PagoV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'
        read_only_fields = 'created_at', 'done_at', 'updated_at'