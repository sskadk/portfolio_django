from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    return render(request,'home.html')
def exp(request):
    experience_show=[
        {"company":"ABC",
         "position":"python developer"},
        {"company":"ABC2",
         "position":"python developer2"},
        {"company":"ABC3",
         "position":"python developer3"},
        {"company":"ABC4",
         "position":"python developer4"},
        {"company":"ABC5",
         "position":"python developer5"},
    ]
    return render(request,'experience.html', {"experience_show":experience_show})


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
    certifications=["HTML - CSS - JavaScript","PHP","Django - Python","React"]
    
    return render(request,'certification.html', {'certifications': certifications})

def resume(request):
    resume_path="cv/cv.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("CV not Found", status=404)