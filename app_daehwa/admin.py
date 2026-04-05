from django.contrib import admin
from .models import Usuario,Chat,Evaluacion_Inicial,Paciente,Diagnostico_Funcional,Plan_Intervencion,Cita,Registro_Sesiones

admin.site.register(Usuario)
admin.site.register(Chat)
admin.site.register(Paciente)
admin.site.register(Evaluacion_Inicial)
admin.site.register(Diagnostico_Funcional)
admin.site.register(Plan_Intervencion)
admin.site.register(Cita)
admin.site.register(Registro_Sesiones)
