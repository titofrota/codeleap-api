from django.urls import path, include
from rest_framework import routers
from api.views import PostViewSet

router = routers.DefaultRouter()

router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
