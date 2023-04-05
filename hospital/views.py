from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from faker import Faker
from .form import PatientForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def patient_list(request):
    data = Patient.objects.all()
    paginator = Paginator(data,10)
    page = request.GET.get('page',1)
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)
    return render(request, 'patients_list.html', {'patients': patients})
    
    #f = Faker()
    #for i in range(10):
    #   patient = Patient(None,f.name(),f.date(),f.boolean())
    #   print (patient.nom)
    #   patient.save()
    
def create_patient(request):
    if request.method == 'POST' :
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(request.POST)
        return render(request, 'create_patient.html',{'form':form})
   
def delete_patient(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    patient.delete()
    return redirect('patient_list')


def update_patient(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(request.POST,instance=patient)
    return render(request, 'update_patient.html',{'form':form, 'patient':patient})

def search(request):
    query = request.GET.get('kw')
    data = Patient.objects.filter(nom__contains=query)
    return render(request, 'patients_list.html', {'patients': data})