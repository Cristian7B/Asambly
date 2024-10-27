from django.shortcuts import render
from .serializers import AsambleaGeneralSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers_get import AsambleaAllSerializer
from Asambly.models import Asamblea, AsambleaParticipante, Votacion, Opcion

class CreateAsamblea(APIView):
    def post(self, request):
        serializer = AsambleaGeneralSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAsambleas(generics.RetrieveAPIView):
    queryset = Asamblea.objects.all()
    serializer_class = AsambleaAllSerializer

class DeleteAsamblea(APIView):
    def delete(self, request):
        try:
            asambleas_id = request.data.get('asambleas_id')
            for asamblea_id in asambleas_id:
                asamblea = Asamblea.objects.get(pk=asamblea_id)
                asamblea.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Asamblea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteParticipanteFromAsamblea(APIView):
    def delete(self, request, pk):
        try:
            asamblea = Asamblea.objects.get(pk=pk)
            participantes_codigo = request.data.get('participantes_codigo')

            for codigo_participante in participantes_codigo:
                try:
                    participante = asamblea.asamblea_participantes.get(codigo_estudiantil=codigo_participante)
                    participante.delete()
                except AsambleaParticipante.DoesNotExist:
                     return Response({'detail': f'Participante con código {codigo_participante} no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
                
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Asamblea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class DeleteVotacionFromAsamblea(APIView):
    def delete(self, request, pk):
        try:
            asamblea = Asamblea.objects.get(pk=pk)
            votaciones_id = request.data.get('votaciones_id')
            
            for id_votacion in votaciones_id:
                try:
                    votacion = asamblea.votaciones.get(pk=id_votacion)
                    votacion.delete()
                except Votacion.DoesNotExist:
                    return Response({'detail': f'Votación con id {id_votacion} no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
                
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Asamblea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteOpcionFromVotacion(APIView):
    def delete(self, request, pk, id_votacion):
        try:
            asamblea = Asamblea.objects.get(pk=pk)

            try:
                votacion = asamblea.votaciones.get(pk=id_votacion)
                opcion = request.data.get('opciones_id')
                for id_opcion in opcion:
                    try:
                        opcion = votacion.opciones.get(pk=id_opcion)
                        opcion.delete()
                    except Opcion.DoesNotExist:
                        return Response({'detail': f'Opción con ID {id_opcion} no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
                
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            except Votacion.DoesNotExist:
                return Response({'detail': f'Votación con ID {id_votacion} no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
            
        except Asamblea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
