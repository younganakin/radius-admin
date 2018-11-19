from rest_framework import serializers
from .models import Radcheck, Nas


class RadcheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radcheck
        fields = ('username', 'value')


class NasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nas
        fields = '__all__'
