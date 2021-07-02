from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def appointment(request):
    return render(request, 'appointment.html', locals())

def blog(request):
    return render(request, 'blog.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())

def gallery(request):
    return render(request, 'gallery.html', locals())

def service(request):
    return render(request, 'service.html', locals())

def team(request):
    return render(request, 'team.html', locals())

def single_blog(request):
    return render(request, 'single-blog.html', locals())