"""
URL configuration for cursos_securitas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('signup/', views.SignupPage, name='signup'),

    #path dos Cursos-Motorista
    path('cursos/cursos-motorista/', views.DriverCourses, name='cursos-motorista'),
    path('cursos/cursos-motorista/curso-nr20/', views.DriverCourses_nr20, name='curso-nr20'),
    #final-path dos Cursos-Motorista

    path('cursos/cursos-ssma/', views.SSMACourses, name='cursos-ssma'),
    path('cursos/cursos-rh/', views.RHCourses, name='cursos-rh'),
    path('cursos/cursos-manutencao/', views.MaintenanceCourses, name='cursos-manutencao'),
    path('cursos/cursos-operacao/', views.OperationCourses, name='cursos-operacao'),
    path('cursos/cursos-financeiro/', views.FinancialCourses, name='cursos-financeiro'),
    path('cursos/cursos-monitoramento/', views.MonitoringCourses, name='cursos-monitoramento'),
    #path dos Videos dos Cursos

    #Path Certificados
    path('generate_certificate_nr20/', views.generate_certificate_nr20, name='generate_certificate_nr20'),
]
