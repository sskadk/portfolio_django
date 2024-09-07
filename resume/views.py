from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def exp(request):
    return render(request,'experience.html')

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'project.html')

def about(request):
    return render(request,'about.html')

def certifications(request):
    return render(request,'certification.html')

# def resume(request):
#     return render(request,'about.html')