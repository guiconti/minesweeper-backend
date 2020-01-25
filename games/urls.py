from django.urls import include, path
from rest_framework import routers
from games.views import GameViewSet

app_name = 'games'

router = routers.DefaultRouter()
router.register(r'games', GameViewSet, basename='games')

urlpatterns = [
  path('v1/', include(router.urls)),
]