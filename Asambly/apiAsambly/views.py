from django.shortcuts import render
from .serializers import AsambleaGeneralSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateAsamblea(APIView):
    def post(self, request):
        serializer = AsambleaGeneralSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)