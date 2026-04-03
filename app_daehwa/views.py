from rest_framework import viewsets
from .models import Usuario,Chat,Evaluacion_Inicial,Paciente,Diagnostico_Funcional,Plan_Intervencion,Cita,Registro_Sesiones
from .serializers import UsuarioSerializer,ChatSerializer,Evaluacion_InicialSerializer,Diagnostico_FuncionalSerializer,Plan_IntervencionSerializer,CitaSerializer,Registro_SesionesSerializer,PacienteSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset=Chat.objects.all()
    serializer_class=ChatSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset=Paciente.objects.all()
    serializer_class=PacienteSerializer

class Evaluacion_InicialViewSet(viewsets.ModelViewSet):
    queryset=Evaluacion_Inicial.objects.all()
    serializer_class=Evaluacion_InicialSerializer

class Diagnostico_FuncionalViewSet(viewsets.ModelViewSet):
    queryset=Diagnostico_Funcional.objects.all()
    serializer_class=Diagnostico_FuncionalSerializer

class Plan_IntervencionViewSet(viewsets.ModelViewSet):
    queryset=Plan_Intervencion.objects.all()
    serializer_class=Plan_IntervencionSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset=Cita.objects.all()
    serializer_class=CitaSerializer

class Registro_SesionesViewSet(viewsets.ModelViewSet):
    queryset=Registro_Sesiones.objects.all()
    serializer_class=Registro_SesionesSerializer