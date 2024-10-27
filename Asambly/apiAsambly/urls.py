from .views import *
from django.urls import path

urlpatterns = [
    path('create-asamblea/', CreateAsamblea.as_view()),
    path('get-asamblea/<int:pk>/', GetAsambleas.as_view()),
]