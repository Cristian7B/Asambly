from django.db import models

class Asamblea(models.Model):
    id_asamblea = models.AutoField(primary_key=True)  
    tema = models.CharField(max_length=50)
    estado = models.CharField(max_length=15)
    informacion_adicional = models.CharField(max_length=1000, blank=True, null=True)
    fecha = models.DateTimeField()

    class Meta:
        db_table = 'asambleas'  

    def __str__(self):
        return self.tema


class Votacion(models.Model):
    id_votacion = models.AutoField(primary_key=True)
    id_asamblea = models.ForeignKey(Asamblea, on_delete=models.CASCADE, related_name='votaciones')
    enunciado_votacion = models.CharField(max_length=100)

    class Meta:
        db_table = 'votaciones'

    def __str__(self):
        return self.enunciado_votacion


class Participante(models.Model):
    codigo_estudiantil = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=30)
    tipo_participante = models.CharField(max_length=15)

    class Meta:
        db_table = 'participantes'

    def __str__(self):
        return self.nombre


class AsambleaParticipante(models.Model):
    id_asam_participantes = models.AutoField(primary_key=True)
    id_asamblea = models.ForeignKey(Asamblea, on_delete=models.CASCADE, related_name='asamblea_participantes')
    codigo_estudiantil = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='asamblea_participantes')

    class Meta:
        db_table = 'asamblea_participantes'

    def __str__(self):
        return f'{self.id_asamblea} - {self.codigo_estudiantil}'


class Intervencion(models.Model):
    id_intervencion = models.AutoField(primary_key=True)
    informacion_intervencion = models.CharField(max_length=500)
    estado_intervencion = models.CharField(max_length=15)
    codigo_estudiantil = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='intervenciones')

    class Meta:
        db_table = 'intervenciones'

    def __str__(self):
        return self.informacion_intervencion


class Opcion(models.Model):
    id_opcion = models.AutoField(primary_key=True)
    id_votacion = models.ForeignKey(Votacion, on_delete=models.CASCADE, related_name='opciones')
    enunciado_opcion = models.CharField(max_length=100)

    class Meta:
        db_table = 'opciones'

    def __str__(self):
        return self.enunciado_opcion


class Voto(models.Model):
    id_voto = models.AutoField(primary_key=True)
    id_opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='votos')

    class Meta:
        db_table = 'voto'

    def __str__(self):
        return f'Voto {self.id_voto} para la opción {self.id_opcion}'
