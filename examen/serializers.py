from rest_framework import serializers
from .models import usuario, servicios, examenes


class pacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = '__all__'

class examenesSerializer(serializers.ModelSerializer):

    class Meta:
        model = examenes
        fields = '__all__'

class agendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = servicios
        fields = '__all__'

