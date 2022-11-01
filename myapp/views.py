from django.contrib import messages
from django.shortcuts import render
from myapp.forms import *
from myapp.models import *

# Create your views here.
from django import forms
import os,uuid


def handle_single_image(f):
    st = str(uuid.uuid4())
    with open('myapp/static/myapp/img/' + "_" + st + ".jpg", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            viewPath = '/static/myapp/img/' + "_" + st + ".jpg"
        return viewPath

def index_page(request):

    if request.method == "POST":
        data = singleImgForm(request.POST, request.FILES)

        if data.is_valid:
            Path = handle_single_image(request.FILES['myImg'])
            save = singleImage(imgname=request.POST['imgname'], myImg=Path)
            save.save()
            messages.success(request, "Data Save Successfully")
            form = singleImgForm()
            all_data = singleImage.objects.all()
            context = {
                "form": form,
                "all_data": all_data,
            }
            return render(request, "myapp/index.html", context)

    form = singleImgForm()
    all_data = singleImage.objects.all()
    context = {
        "form": form,
        "all_data":all_data,
    }
    return render(request, "myapp/index.html",context)



