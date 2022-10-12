from rest_framework import routers
from .api import EstudianteViewSet, ConductorViewSet, PersonaViewSet, ListaViewSet, RutaViewSet

router = routers.DefaultRouter()

router.register('api/Estudiante',EstudianteViewSet, 'proyecto/Estudiante')
urlpatterns = router.urls

router.register ('api/Conductor',ConductorViewSet, 'proyecto/Conductor')
urlpatterns = router.urls

router.register('api/Persona',PersonaViewSet, 'proyecto/Persona')
urlpatterns = router.urls

router.register('api/Lista',ListaViewSet, 'proyecto/Lista')
urlpatterns = router.urls

router.register('api/Ruta',RutaViewSet, 'proyecto/Ruta')
urlpatterns = router.urls