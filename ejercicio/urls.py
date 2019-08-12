from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from checador.views import RegistroViewSet
from checador.views import IncidenciaViewSet
from checador.views import MeseViewSet
from suc.views import SucursalViewSet
from accounts.views import ProfileViewSet

checador=routers.DefaultRouter()
suc=routers.DefaultRouter()
accounts=routers.DefaultRouter()

checador.register('registros-de-entradas',RegistroViewSet)
checador.register('registros-de-incidencias',IncidenciaViewSet)
checador.register('registros-de-incidencia-mes',MeseViewSet)
suc.register('sucursales',SucursalViewSet)
accounts.register('perfiles',ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checador/', include(checador.urls)),
    path('suc/', include(suc.urls)),
    path('accounts/', include(accounts.urls))
]
