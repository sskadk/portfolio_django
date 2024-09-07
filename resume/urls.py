from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('exp', views.exp, name='experience'),
    # path('resume', views.resume, name='resume'),
    path('certifications', views.certifications, name='certifications'),
]
