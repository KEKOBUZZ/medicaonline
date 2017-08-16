from rest_framework import serializers
from medica_app.models import Paciente, Medico, Cita, Consultorio, Historial


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id', 'name', 'last_name','gender','age','phone','adress','postal_code','email','password')

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id', 'name', 'last_name','gender','age','professional_id','phone','email','password')

class CitaSerializer(serializers.ModelSerializer):
    #paciente = PacienteSerializer()
    #medico = MedicoSerializer()
    class Meta:
    	model = Cita
    	fields = ('id', 'paciente', 'medico','date')

class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = ('id', 'medico', 'adress','postal_code')

class HistorialSerializer(serializers.ModelSerializer):
    #cita = CitaSerializer()
    class Meta:
    	model = Historial
    	fields = ('id', 'cita', 'observaciones')