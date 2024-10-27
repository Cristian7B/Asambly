from rest_framework import serializers
from Asambly.models import Asamblea, Participante, AsambleaParticipante, Intervencion, Votacion, Opcion

class OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ["id_opcion", "enunciado_opcion"]

class VotacionesSerializer(serializers.ModelSerializer):
    opciones = OpcionesSerializer(many=True)

    class Meta:  
        model = Votacion
        fields = ["id_votacion", "enunciado_votacion", "opciones"]

class IntervencionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervencion
        fields = ["id_intervencion", "informacion_intervencion", "estado_intervencion"]

class ParticipantesSerializer(serializers.ModelSerializer):
    intervenciones = IntervencionesSerializer(many=True)

    class Meta:
        model = Participante
        fields = ["codigo_estudiantil", "nombre", "tipo_participante", "intervenciones"]

class AsambleaParticipanteSerializer(serializers.ModelSerializer):
    participante = ParticipantesSerializer(source='codigo_estudiantil', read_only=True)

    class Meta:
        model = AsambleaParticipante
        fields = ['participante']


class AsambleaAllSerializer(serializers.ModelSerializer):
    participantes_data = AsambleaParticipanteSerializer(many=True, source='asamblea_participantes', read_only=True)

    class Meta:
        model = Asamblea
        fields = ['tema', 'estado', 'informacion_adicional', 'fecha', 'participantes_data']

