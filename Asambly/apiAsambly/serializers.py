from rest_framework import serializers
from Asambly.models import Asamblea, Participante, AsambleaParticipante, Intervencion, Votacion, Opcion

class OpcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['enunciado_opcion']

class VotacionSerializer(serializers.ModelSerializer):
    opciones = OpcionesSerializer(many=True)

    class Meta:
        model = Votacion
        fields = ['enunciado_votacion', 'opciones']

class AsambleaGeneralSerializer(serializers.ModelSerializer):
    participantes_data = serializers.ListField(
        child=serializers.DictField(),  
        write_only=True 
    )

    votaciones_data = VotacionSerializer(many=True, write_only=True)

    class Meta:
        model = Asamblea
        fields = ['tema', 'estado', 'informacion_adicional', 'fecha', 'participantes_data', 'votaciones_data']

    def create(self, validated_data):
        participantes_data = validated_data.pop('participantes_data')
        votaciones_data = validated_data.pop('votaciones_data', []) 
        
        asamblea = Asamblea.objects.create(**validated_data)

        for votacion_data in votaciones_data:
            votacion_creada = Votacion.objects.create(
                id_asamblea=asamblea,
                enunciado_votacion=votacion_data.get("enunciado_votacion")
            )

            opciones_data = votacion_data.get("opciones", [])

            for opcion_data in opciones_data:
                Opcion.objects.create(
                    id_votacion=votacion_creada,
                    **opcion_data
                )

        for participante in participantes_data:
            codigo_estudiantil = participante.get("codigo_estudiantil")
            participante_creado, _ = Participante.objects.get_or_create(
                codigo_estudiantil=codigo_estudiantil,
                defaults={
                    "nombre": participante.get("nombre"),
                    "tipo_participante": participante.get("tipo_participante")
                }
            )

            intervenciones = participante.get("intervencion", [])
            for intervencion_data in intervenciones:
                Intervencion.objects.create(
                    codigo_estudiantil=participante_creado,
                    **intervencion_data
                )

            AsambleaParticipante.objects.create(
                id_asamblea=asamblea,
                codigo_estudiantil=participante_creado
            )

        return asamblea
