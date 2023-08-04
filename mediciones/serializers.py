from rest_framework import serializers

from .models import Area, Region, Measurements

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
     # las siguiente linea seria si solo quieres algunos campos del modelo
    #    fields = [' id', 'name', 'owner', ]
        model = Area
        fields = '__all__'
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
         model = Region
         fields = '__all__'
class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'

