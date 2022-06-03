
from django.urls import path, include
from .views import PlayerDetailsView, matchDetailsView, matchNoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('players-list', PlayerDetailsView, basename='players-details')
router.register('match-list', matchNoView, basename='match-list')
router.register('match-details', matchDetailsView, basename='match-details')

urlpatterns = [
    path('', include(router.urls)),
]