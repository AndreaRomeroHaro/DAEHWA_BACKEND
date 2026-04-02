from django.contrib import admin
from .models import Usuario,Chat,Evaluacion_Inicial,Paciente,Diagnostico_Funcional,Plan_Intervencion,Cita,Registro_Sesiones

admin.register(Usuario)
admin.register(Chat)
admin.register(Paciente)
admin.register(Evaluacion_Inicial)
admin.register(Diagnostico_Funcional)
admin.register(Plan_Intervencion)
admin.register(Cita)
admin.register(Registro_Sesiones)
