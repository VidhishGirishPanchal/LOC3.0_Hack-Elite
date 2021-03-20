from django.shortcuts import render
from account.models import Doctor,Patient
from .models import *

# Create your views here.

def about(request):
    return render(request,'about.html')

def display_doctors(request,specialization):
    specialization = specialization.lower()
    doctors = Doctor.objects.filter(specialization=specialization,is_verified=True)
    return render(request,'doctors.html',{'doctors':doctors})

def book_appointment(request,doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    patient = Patient.objects.get(email=request.user)
    Appointment.objects.create(patient=patient,doctor=doctor)

    return render(request,'doctors.html')

def doctor_type(request):
    specializations = Specialization.objects.all()
    return render(request,'selecttypeofdoctor.html',{'specializations':specializations})