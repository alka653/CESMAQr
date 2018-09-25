from django.contrib.auth.decorators import login_required
from django.conf.urls import url, patterns
from .views import *

urlpatterns = patterns('codigoQR.apps.home.views',
	url(r'^(?P<identificacion>\d+)/$', login_required(TakeInOutQR.as_view()), name = 'toma_codigo_qr'),
	url(r'^reporte/$', login_required(MakeReporte.as_view()), name = 'reporte_codigo_qr'),
	url(r'^reporte/pdf/$', login_required(FacturaPDFView.as_view()), name = 'reporte_pdf_codigo_qr')
)