from django.urls import path

from . import views

urlpatterns = [
    path('consultas/', views.getConsulta, name='getConsulta'),
]
