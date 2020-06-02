from django.shortcuts import render
from .forms import StudentRegistration ,FormFieldWithArguments

def index(request):
    return render(request,'student/index.html')

def showFormData(request):
    fm=StudentRegistration()
    context={'form':fm}
    return render(request,'student/register.html',context)

def formFieldwithAguments(request):
    #fm=FormFieldWithArguments(initial= {'name':'abc','address':'Toppura'})
    fm=FormFieldWithArguments()
    context={'form':fm}
    return render(request,'student/form_field_with_arguments.html',context)