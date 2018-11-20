from rest_framework import serializers
from .models import Radcheck, Nas


class RadcheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radcheck
        fields = '__all__'


class NasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nas
        fields = '__all__'
