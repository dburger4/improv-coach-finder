from rest_framework import serializers
from .models import ImprovCoach

class ImprovCoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImprovCoach 
        fields = ('pk', 'firstname', 'lastname', 'phone', 'joined_date')