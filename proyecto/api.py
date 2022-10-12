from .models import Estudiante, Conductor, Persona, lista, Ruta
from .serializers import EstudianteSerializer,ConductorSerializer, PersonaSerializer, ListaSerializer, RutaSerializer
from rest_framework import viewsets, permissions

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstudianteSerializer

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConductorSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ListaSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RutaSerializer
