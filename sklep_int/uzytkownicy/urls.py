from rest_framework import routers
from django.urls import include,path
from .views import ButyViewSet

router = routers.DefaultRouter()
router.register(r'Buty',ButyViewSet)
#router.register(r'Ocena',OcenaViewSet)



urlpatterns= [ 
    path('api/',include(router.urls)),
    path('api-aut/', include('rest_framework.urls', namespace='rest_framework'))]