from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import *

#-------------------------------------------------------------------------------------------------------------------------
def service_signup(request):
    if request.method=='POST':
        form=ServiceUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            

            my_shop_group=Group.objects.get_or_create(name='SERVICE')
            my_shop_group[0].user_set.add(user)

        

            return HttpResponseRedirect('service_login')
    else:
        form=ServiceUserForm()
        
    return render(request, 'service/service_signup.html',{'form':form})

def service_login(request):
    if request.method == 'POST':
        form = ServiceLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.groups.filter(name='SERVICE'):
                    #if shop_user.objects.all().filter(user_id=user.id):
                    login(request,user)
                    return redirect('upload_img')
                    #else:
                       #messages.success(request, 'Your Request is in process, please wait for Approval..') 
                else:
                    messages.success(request, 'Your account is not found')
            else:
                messages.success(request, 'Your Username and Password is Wrong..')
    else:
         form = ServiceLoginForm()           
    return render(request, 'service/service_login.html',{'form':form})

@login_required(login_url='service_login')
def service_home(request):
    return render(request,'service/service_home.html')

def logout_view(request):
    logout(request)
    return redirect('homepagess')


#####################################################################
from PIL import Image,ImageEnhance
import pytesseract
import cv2
import numpy as np

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image = Image.open(filename)
    img = np.array(image)
    grayscale = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    adaptive = cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,71,11)
    text = pytesseract.image_to_string(adaptive)
    #text = pytesseract.image_to_string(Image.open(filename)) # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text


# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'
@login_required(login_url='service_login')
def upload_page(request):
    cus = request.user
    if request.method == 'POST':
        
        
        if 'file' not in request.FILES:
            return render(request,'service/upload.html')
        file = request.FILES['file']
        
        extracted_text = ocr_core(file)
        scan = Comp(image= file,snum=extracted_text,cus_id=cus)
        scan.save()
        #txt = extracted_text.split()
        
        return render(request,'service/upload.html',
                                   {'extracted_text':extracted_text},
                                   )
        
    elif request.method == 'GET':
        return render(request,'service/upload.html')

####################################################################################

@login_required(login_url='service_login')
def scan_view(request):
    id = request.user
    s = Comp.objects.all().filter(cus_id_id = id)


    return render(request,'service/scan_view.html',{'s':s})
@login_required(login_url='service_login')
def sales(request):
    id = request.user
    s = Comp.objects.all().filter(cus_id_id = id)
    # for i in s:
    #     ext  = i.snum
    #     txt = ext.split()
        
        
        # txt = ext.split()
        # print(txt)
            
    return render(request,'service/sales.html',{'s':s})

@login_required(login_url='service_login')
def profile_view(request):
    return render(request,'service/profile.html')

