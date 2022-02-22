from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Image
from . form import ImageForm

# Create your views here.

def home(request):
    return render(request, "webapp/index.html")


def Ourgallery(request):
    if request.method == 'POST':
        form = ImageForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'webapp/gallery.html', {"obj":obj})

    else:
        form = ImageForm()
        img = Image.objects.all()
    return render(request, 'webapp/gallery.html', {'img':img, 'form':form})