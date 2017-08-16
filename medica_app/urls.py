from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from medica_app import views

urlpatterns = [
    url(r'^paciente/$', views.PacienteList.as_view()),
    url(r'^paciente/(?P<pk>[0-9]+)/$', views.PacienteDetail.as_view()),
    url(r'^medico/$', views.MedicoList.as_view()),
    url(r'^medico/(?P<pk>[0-9]+)/$', views.MedicoDetail.as_view()),
    url(r'^cita/$', views.CitaList.as_view()),
    url(r'^cita/(?P<pk>[0-9]+)/$', views.CitaDetail.as_view()),
    url(r'^consultorio/$', views.ConsultorioList.as_view()),
    url(r'^consultorio/(?P<pk>[0-9]+)/$', views.ConsultorioDetail.as_view()),
    url(r'^historial/$', views.HistorialList.as_view()),
    url(r'^historial/(?P<pk>[0-9]+)/$', views.HistorialDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)