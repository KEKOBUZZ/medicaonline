from medica_app.models import Paciente, Medico, Cita, Consultorio, Historial
from medica_app.serializers import PacienteSerializer, MedicoSerializer, CitaSerializer, ConsultorioSerializer, HistorialSerializer
from rest_framework import generics

class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoList(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class MedicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class CitaList(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


class CitaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class ConsultorioList(generics.ListCreateAPIView):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer


class ConsultorioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer

class HistorialList(generics.ListCreateAPIView):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer


class HistorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer




