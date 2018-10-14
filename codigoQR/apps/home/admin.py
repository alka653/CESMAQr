from django.contrib import admin

from.models import *

admin.site.register(Registros)
admin.site.register(Grados)

class EstudiantesAdmin(admin.ModelAdmin):
	fields = ('identificacion', 'nombre', 'grado')
	list_display = ('identificacion', 'nombre', 'grado', 'codigoQR')
	search_fields = ('identificacion', 'nombre', 'grado')

	def codigoQR(self, obj):
		return '<div id="id-'+obj.identificacion+'"><button id="btn-'+obj.identificacion+'" style="padding: 8px; border: none; color: white; background-color: #999; cursor: pointer; border-radius: 15px;" type="button" onclick="handleCodigoQR('+obj.identificacion+')">Generar QR</button></div>'

	codigoQR.allow_tags = True

admin.site.register(Estudiantes, EstudiantesAdmin)