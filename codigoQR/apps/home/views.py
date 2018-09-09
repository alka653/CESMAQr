# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *

class TakeInOutQR(TemplateView):
	template_name = 'take_code_qr.html'

	def get_context_data(self, **kwargs):
		msg = ''
		type_msg = 'success'
		context = super(TakeInOutQR, self).get_context_data(**kwargs)
		estudiante = Estudiantes.objects.filter(identificacion=self.kwargs['identificacion'])
		if estudiante.count() > 0:
			mode = 'I'
			type_msg = 'success'
			estudiante = estudiante[0]
			msg = 'Ingreso del estudiante '+estudiante.nombre+' realizado'
			query = Registros.objects.filter(estudiante=estudiante).order_by('-pk')
			if query.count() > 0:
				if query.first().mode == 'I':
					mode = 'S'
					msg = 'Salida del estudiante '+estudiante.nombre+' realizado'
			registro = Registros(estudiante=estudiante, mode = mode)
			registro.save()
		else:
			type_msg = 'danger'
			msg = 'Estudiante no encontrado'
		context['message'] = msg
		context['type'] = type_msg
		return context