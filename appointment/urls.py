from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.about,name='about'),
    path('doctor-type',views.doctor_type,name='doctor_type'),
    path('display-doctors/<specialization>',views.display_doctors,name='display_doctors'),
    path('boook-appointment/<doctor_id>',views.book_appointment,name='book_appointment'),

    
]
