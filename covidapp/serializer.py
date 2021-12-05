from rest_framework import fields,serializers

from .models import *

class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = countries
        fields = ['ID','CountryCode','Country','NewConfirmed','TotalConfirmed','NewDeaths','TotalDeaths','NewRecovered','TotalRecovered']
