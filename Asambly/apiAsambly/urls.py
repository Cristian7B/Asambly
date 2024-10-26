from .views import *
from django.urls import path

urlpatterns = [
    path('create-asamblea/', CreateAsamblea.as_view()),
]