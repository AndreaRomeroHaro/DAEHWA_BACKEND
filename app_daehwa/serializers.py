from rest_framework import serializers
from .models import Usuario,Chat,Evaluacion_Inicial,Paciente,Diagnostico_Funcional,Plan_Intervencion,Cita,Registro_Sesiones

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=['id','nombre','correo_electronico','rol','foto_usuario']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields="__all__"

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields='__all__'
    
class Evaluacion_InicialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Evaluacion_Inicial
        fields="__all__"

class Diagnostico_FuncionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Diagnostico_Funcional
        fields="__all__"

class Plan_IntervencionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan_Intervencion
        fields="__all__"

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cita
        fields="__all__"

class Registro_SesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro_Sesiones
        fields="__all__"
