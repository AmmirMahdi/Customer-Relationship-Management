from rest_framework import serializers
from .models import Opportinuty

class OpportinutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportinuty
        fields = ['name',"account","stage","lead_source","probility","contacs","closed_by","description","cteated_by","is_activype"]
