from rest_framework.serializers import ModelSerializer
from .models import Atama


class AtamaSerializer(ModelSerializer):
    class Meta:
        model = Atama
        fields = "__all__"