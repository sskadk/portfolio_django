from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def exp(request):
    return render(request,'experience.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    projects_show=[
        {"title":"E-commerce Website",
         "path":"img/ecom.jpg"},
        {"title":"Portfolio Website",
         "path":"img/port.jpg"},
        {"title":"News Portal Website",
         "path":"img/np.jpg"},
        {"title":"Blogs Website",
         "path":"img/blog.jpg"},
        {"title":"Real Estate Website",
         "path":"img/rs.jpg"},
    ]
    return render(request,'project.html', {"projects_show": projects_show})

def certifications(request):
    return render(request,'certification.html')

# def resume(request):
#     return render(request,'about.html')