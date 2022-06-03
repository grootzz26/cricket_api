from django.urls import path
from .views import RegiaterView

urlpatterns = [
    path('register/', RegiaterView, name='user-register'),
]