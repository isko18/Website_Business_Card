from django.shortcuts import render
from .models import Settings, Blog, Contact

def index(request):
    settings = Settings.objects.all()
    return render(request, 'index.html', {'settings': settings})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def contact(request):
    contact = Contact.objects.first()
    return render(request, 'contact.html', {'contact': contact})

