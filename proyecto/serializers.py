from rest_framework import serializers
from .models import Persona,Estudiante,Conductor,lista,Ruta


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id_persona', 'nombre_persona', 'cedula_persona', 'telefono_persona')

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id', 'codigo_universitario', 'correo_institucional', 'persona')

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = ('id', 'horario','persona')

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ('id', 'numero_ruta', 'estado_ruta', 'recorrido_ruta', 'Conductor')

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = lista
        fields = ('id', 'plaza_dis', 'horario_salida', 'estudiante', 'ruta')