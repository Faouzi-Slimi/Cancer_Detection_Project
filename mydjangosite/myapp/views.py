from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *
import os
from django.core.files.storage import FileSystemStorage
from .functions import f_pred
from . import forms, models
from django.http import HttpResponse
from django.template import loader
import shutil


from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'myapp/login.html')


def html(request):
    return render(request, 'myapp/Main_App.html')



def upload_image(request,*kwargs):
    for t in os.listdir(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\media\media'):
        url = os.getcwd() + "\\media\\media\\" + str(t)
        os.remove(url)

    for t in os.listdir(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\static\img'):
        url = os.getcwd()+"\\static\\img\\"+str(t)
        os.remove(url)




    if request.method == "POST":

        # process POST request
         files = request.FILES  # multivalued dict
         image = files.get("image")
         instance = ImageModel()
         instance.image = image
         instance.save()
         template = loader.get_template('myapp/Main_App.html')
         for t in os.listdir(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\media\media'):
             url1 = os.getcwd() + "\\media\\media\\" + str(t)
             url2 = os.getcwd() + "\\static\\img\\" + str(t)
             shutil.copy(url1, url2)
         a='0'
         b='9'
         for t in os.listdir(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\static\img'):
             context = {
                'url': 'img/'+str(t),
                 'url1' : 'init/interog.jfif'


             }

         return HttpResponse(template.render(context, request))

def Predict(request,*kwargs):
    if request.method == "POST":
        template = loader.get_template('myapp/Main_App.html')
        for t in os.listdir(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\static\img'):
            context = {
                'url': 'img/' + str(t),
            }
        url_img = r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\static\img\\'+t

        if f_pred(url_img) :

          context['url1']= 'init/False.png'
        else :
          context['url1'] = 'init/Truee.jfif'

        return HttpResponse(template.render(context, request))
def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)

        if user is not None:
            # Success, now let's login the user.

            template = loader.get_template('myapp/Main_App.html')
            context = {
                'url': 'init/cancer.jpg',
                'url1': 'init/interog.jfif',
            }
            return HttpResponse(template.render(context, request))
        else:
            return redirect("/", custom_error="Try Again Later")




def Main_App(request):
    return render(request, "myapp/Main_App.html")

