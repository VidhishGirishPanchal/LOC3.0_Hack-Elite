from django.shortcuts import render
from account.models import Doctor,Patient
from .models import *

# Create your views here.

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home4.html')

def patientdashboard(request):
    return render(request,'patientdashboard.html')

def doctordashboard(request):
    return render(request,'doctordashboard.html')

def patientcompletedappointments(request):
    return render(request,'patientcompletedappointments.html')

def pendingappointments(request):
    return render(request,'pendingappointments.html')

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

def blog(request):
    Posts=Post.objects.all()
    return render(request,"blog.html",{'allPosts':Posts})