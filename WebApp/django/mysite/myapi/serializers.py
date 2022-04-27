from .models import Hero, Villain 
from rest_framework import serializers 

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero 
        fields = ('name', 'alias')

class VillainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Villain
        fields = ('name', 'alias')
