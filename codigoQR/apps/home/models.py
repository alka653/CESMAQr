from django.db import models

class Grados(models.Model):
	nombregrado=models.CharField(max_length=10)

	def __str__(self):
		return self.nombregrado

	def __unicode__(self):
		return self.nombregrado

class Estudiantes(models.Model):
	nombre=models.CharField(max_length=50)
	identificacion=models.CharField(max_length=15, unique=True)
	grado=models.ForeignKey(Grados)

	def __str__(self):
		return self.identificacion+' - '+self.nombre+' - '+self.grado.nombregrado

	def __unicode__(self):
		return self.identificacion+' - '+self.nombre+' - '+self.grado.nombregrado

class Registros(models.Model):
	fecha_ingreso_salida=models.DateTimeField(auto_now=True)
	mode=models.CharField(max_length=1)
	estudiante=models.ForeignKey(Estudiantes)

	class Meta:
		ordering = ['-fecha_ingreso_salida']

	def __str__(self):
		return str(self.fecha_ingreso_salida.strftime("%Y-%m-%d %H:%M"))+' - '+('Ingreso' if self.mode == 'I' else 'Salida')+' - '+self.estudiante.nombre

	def __unicode__(self):
		return str(self.fecha_ingreso_salida.strftime("%Y-%m-%d %H:%M"))+' - '+('Ingreso' if self.mode == 'I' else 'Salida')+' - '+self.estudiante.nombre