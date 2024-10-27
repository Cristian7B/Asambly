from .views import *
from django.urls import path

urlpatterns = [
    path('create-asamblea/', CreateAsamblea.as_view()),
    path('get-asamblea/<int:pk>/', GetAsambleas.as_view()),
    path('delete-asamblea/', DeleteAsamblea.as_view()),
    path('delete-votacion/<int:pk>/', DeleteVotacionFromAsamblea.as_view()),
    path('delete-opcion/<int:pk>/<int:id_votacion>/', DeleteOpcionFromVotacion.as_view()),
    path('delete-participante/<int:pk>/', DeleteParticipanteFromAsamblea.as_view()),
    path('update-asamblea/<int:pk>/', UpdateAsamblea.as_view()),
]   