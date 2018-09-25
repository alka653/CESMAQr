# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView, FormView
from easy_pdf.views import PDFTemplateView
from django.shortcuts import render
from .models import *
from .forms import*

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

class MakeReporte(FormView):
	form_class = ReporteForm
	template_name = 'form_reporte.html'

class FacturaPDFView(PDFTemplateView):
	template_name = "pdf.html"

	def get_context_data(self, **kwargs):
		context = super(FacturaPDFView, self).get_context_data(**kwargs)
		query = Registros.objects.filter(fecha_ingreso_salida__range = (self.request.GET.get('fecha_inicio'), self.request.GET.get('fecha_final')))
		if self.request.GET.get('estudiante') != '':
			query = query.filter(estudiante__id = self.request.GET.get('estudiante'))
		context['fecha_inicio'] = self.request.GET.get('fecha_inicio')
		context['fecha_final'] = self.request.GET.get('fecha_final')
		context['query'] = query
		return context