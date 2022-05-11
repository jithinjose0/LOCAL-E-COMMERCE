from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from numpy import append
from .form import shopUserForm,shopExtraForm,shopLoginForm,productform
from .models import shop_user
from store.models.product import Products
from store.models.orders import Order
#-------------------------------SHOP signup,login,home-----------------------------------------------------
def shop_signup(request):
    if request.method=='POST':
        form1=shopUserForm(request.POST)
        form2=shopExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()

            my_shop_group=Group.objects.get_or_create(name='SHOP')
            my_shop_group[0].user_set.add(user)

        

            return HttpResponseRedirect('shop_login')
    else:
        form1=shopUserForm()
        form2=shopExtraForm()
    return render(request, 'customers/shop_signup.html',{'form1':form1,'form2':form2})
def shop_login(request):
    if request.method == 'POST':
        form = shopLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.groups.filter(name='SHOP'):
                    if shop_user.objects.all().filter(user_id=user.id):
                        login(request,user)
                        return redirect('dashboard')
                    #else:
                       #messages.success(request, 'Your Request is in process, please wait for Approval..') 
                else:
                    messages.success(request, 'Your account is not found')
            else:
                messages.success(request, 'Your Username and Password is Wrong..')
    else:
         form = shopLoginForm()           
    return render(request, 'customers/shop_login.html',{'form':form})

@login_required(login_url='shop_login')
def shop_home(request):
    name = request.user.id
    shop = request.user.shop_user.id
    #product = Products.objects.filter(shops=name)
    #ordered_list = Order.objects.filter(shop=shop_name)
    print(ordered_list)
    return render(request, 'customers/shop_home.html',{'name':name,'shop':shop})

@login_required(login_url='shop_login')
def allproducts(request):
    name = request.user.id
    shop_name = request.user.shop_user.id
    product = Products.objects.filter(shops=name)
    #ordered_list = Order.objects.filter(shop=shop_name)
    #print(ordered_list)
    return render(request, 'customers/allproducts.html',{'product':product})

@login_required(login_url='shop_login')
def ordered_list(request):
    name = request.user.id
    shop_name = request.user.username
    #product = Products.objects.filter(shops=name)
    ordered_list = Order.objects.filter(shopss=shop_name)
    #print(ordered_list)
    return render(request, 'customers/ordered_list.html',{'ordered_list':ordered_list})

def samdash(request):
    return render(request,'customers/samdash.html')

def about(request):
    return render(request,'home/about.html')
def contact(request):
    return render(request,'home/contact.html')

#------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='shop_login')
def regproducts(request):
    if request.method == 'POST':
        forms = productform(request.POST, request.FILES)
        if forms.is_valid():
            instance=forms.save(commit=False)
            instance.shops = request.user
            instance.save()
            print('successssssss')
            return redirect('allproducts')
    else:
        forms=productform()
    return render(request,'customers/register_products.html',{'forms':forms})


def sample(request):
    pro =Products.objects.all()
    return render(request,'customers/sample.html',{'pro':pro})
#    errorrrrrr
def findingshop(request):
    finds = shop_user.objects.all()
    prod = Products.objects.all()
    
    for i in prod:
        a=i.shops
        pro=a
        print(pro)
        #pro = shop_user.objects.filter(user=a)
        #print(pro)

    return render(request,'customers/findshop.html',{'finds':finds,'prod':prod,'pro':pro})

def homepage(request):
    return render(request,'home/index.html')
def index(request):
    return render(request,'dashhome/index.html')

#------------------------------Data Science---------------------------------------------------------------------------------------------------------

#------------------------------Data Science----------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
from .models import *
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64
import seaborn as sns

@login_required(login_url='shop_login')
def dashboard(request):
    shops = request.user.username
    datas = data.objects.all().filter(shop=shops)
    if datas:
        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Order_Date'] = pd.to_datetime(all_data['Order_Date'],  errors='coerce', format ='%m/%d/%Y %H:%M')
        all_data['Month'] = pd.to_datetime(all_data['Order_Date']).dt.year

        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
        all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
        all_data = all_data.groupby(['Month']).sum()

        months = range(2013,2022)
        plt.bar(months,all_data.groupby(['Month']).sum()['Sales'])
        plt.xticks(months)
        plt.ylabel('Sales in USD (Million)')
        plt.xlabel('Year')
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf,format= 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri1 = urllib.parse.quote(string)
        plt.close()
        

        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Order_Date'] = pd.to_datetime(all_data['Order_Date'],  errors='coerce', format ='%m/%d/%Y %H:%M')
        p = all_data[all_data['Order_Date'].dt.strftime('%Y') == '2021']
        all_data['Month'] = pd.to_datetime(p['Order_Date']).dt.month

        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
        all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
        all_data = all_data.groupby(['Month']).sum()

        months = range(1,13)
        plt.plot(months,all_data.groupby(['Month']).sum()['Sales'])
        plt.xticks(months)
        plt.ylabel('')
        plt.xlabel('Month number(2021)')
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf,format= 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri2 = urllib.parse.quote(string)
        plt.close()

        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        p=len(all_data.index)

        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all = all_data['Quantity'].sum()
        #print(all)
        context = {
            'data1' : uri1,
            'data2' : uri2,
            'p' : p,
            'all':all,
            
        }
        return render(request,'customers/dashboard.html',context)
    else:
        
        return redirect('regproduct')
    


@login_required(login_url='shop_login')
def pro_list(request):
    shops = request.user.username
    datas = data.objects.all().filter(shop=shops)
    if datas:
        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all_data = all_data.groupby(['Product']).sum()

        keys = [pair for pair, df in all_data.groupby(['Product'])]
        plt.bar(keys, all_data.groupby(['Product']).sum()['Quantity'],color='g')
        plt.xticks(keys, rotation='vertical', size=7)
        fig = plt.gcf().subplots_adjust(bottom=0.35)
        buf = io.BytesIO()
        plt.savefig(buf,format= 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        plt.close()
    
        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
        keys = [pair for pair, df in all_data.groupby(['Product'])]

        # Why do you think it sold the most?
        prices = all_data.groupby(['Product']).mean()['Price_Each']

        fig, ax1 = plt.subplots()

        ax2 = ax1.twinx()
        ax1.bar(keys, all_data.groupby(['Product']).sum()['Quantity'], color='g')
        ax2.plot(keys, prices, color='b')

        
        ax1.set_ylabel('Quantity Ordered', color='g')
        ax2.set_ylabel('Price ($)', color='b')
        ax1.set_xticklabels(keys, rotation='vertical', size=7)

        
        fig = plt.gcf().subplots_adjust(bottom=0.35)
        buf = io.BytesIO()
        plt.savefig(buf,format= 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri1 = urllib.parse.quote(string)
        plt.close()

        context = {
            'data' : uri,
            'data1': uri1,        
            
        }
        return render(request,'customers/pro_list.html',context)
    else:
        
        return render(request,'customers/sorry.html')


def get_city(address):
    return address.split(",")[1].strip(" ")
def get_state(address):
    return address.split(",")[2].split(" ")[1]
@login_required(login_url='shop_login')
def city(request):
    shops = request.user.username
    datas = data.objects.all().filter(shop=shops)
    if datas:
        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Order_Date'] = pd.to_datetime(all_data['Order_Date'],  errors='coerce', format ='%m/%d/%Y %H:%M')
        all_data['Month'] = pd.to_datetime(all_data['Order_Date']).dt.month
        all_data['City'] = all_data['Purchase_Address'].apply(lambda x: f"{get_city(x)}  ({get_state(x)})")
        # What was the best month for sales? How much was earned that mont
        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
        all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
        # What city sold the most product?, , size=8
        all_data=all_data.groupby(['City']).sum()
        #print(all_data)
        keys = [city for city, df in all_data.groupby(['City'])]

        plt.bar(keys,all_data.groupby(['City']).sum()['Sales'])
        plt.ylabel('Sales in USD (Million)')
        plt.xlabel('')
        plt.xticks(rotation='vertical',size=7)
        fig = plt.gcf().subplots_adjust(bottom=0.22)
        buf = io.BytesIO()
        plt.savefig(buf,format= 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        plt.close()
        
        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Order_Date'] = pd.to_datetime(all_data['Order_Date'],  errors='coerce', format ='%m/%d/%Y %H:%M')
        all_data['Month'] = pd.to_datetime(all_data['Order_Date']).dt.year

        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
        all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
        all_data = all_data.groupby(['Month']).sum()

        months = range(2013,2022)
        #sns.barplot(x='months',y='all_data')
        #plt.xticks(rotation = 'vertical')
        plt.plot(months,all_data.groupby(['Month']).sum()['Sales'],color='b')
        plt.xticks(months)
        plt.ylabel('Sales in USD (Million)')
        plt.xlabel('Year')
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf,format= 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri1 = urllib.parse.quote(string)
        plt.close()
        context = {
            'data' : uri,
            'data1': uri1,
            
            
        }
        return render(request,'customers/city.html',context)
    else:
        
        return render(request,'customers/sorry.html')


############################################MMMMMMMMMMLLLLLLLL#################################################


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
from pandas.tseries.offsets import DateOffset

@login_required(login_url='shop_login')
def mls(request):
    shops = request.user.username
    datas = data.objects.all().filter(shop=shops)
    if datas:
        shops = request.user.username
        all_data = data.objects.all().filter(shop=shops).values()
        all_data = pd.DataFrame(all_data)
        all_data['Order_Date'] = pd.to_datetime(all_data['Order_Date'],  errors='coerce', format ='%m/%d/%Y %H:%M')
        all_data['month_year'] = pd.DatetimeIndex(all_data['Order_Date']).to_period("M")
        print(all_data['month_year'])
        #all_data['Month'] = pd.to_datetime(all_data['Order_Date']).dt.month
        #all= all_data.groupby(['Year'],['Month'])
        
        all_data.set_index('month_year',inplace=True)
        all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
        all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
        all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
        all_data['Sales']=pd.to_numeric(all_data['Sales'])
        all = pd.DataFrame(all_data.groupby(['month_year']).sum()['Sales'])
        print(all['Sales'])

        #all['month_year'] = pd.to_datetime(all['month_year'])
        all['Sales'] = pd.to_numeric(all['Sales'])
        #all= all.columns=["month_year","Sales"]
        #print(all['Sales'])
        # all['month_year'] = pd.to_datetime(all['month_year'])
        # all.set_index('month_year',inplace=True)
        all['Seasonal First Difference']=all['Sales']-all['Sales'].shift(12)
        print(all.head(14))
        model=ARIMA(all['Sales'],order=(1,1,1))
        model_fit=model.fit()
        
        all['forecast']=model_fit.predict(start=90,end=103,dynamic=True)
        

        model=sm.tsa.statespace.SARIMAX(all['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
        results=model.fit()
        all['forecast']=results.predict(start=90,end=103,dynamic=True)
        #all[['Sales','forecast']].plot(figsize=(12,8))
        future_dates=[all.index[-1] + x for x in range(0,24)]
        
        future_datest_df=pd.DataFrame(index=future_dates[1:],columns=all.columns)
        future_df=pd.concat([all,future_datest_df])
        future_df['forecast'] = results.predict(start = 104, end = 120, dynamic= True)  
        future_df[['Sales', 'forecast']].plot(figsize=(12, 8)) 

        fig = plt.gcf().subplots_adjust(bottom=0.22)
        buf = io.BytesIO()
        plt.savefig(buf,format= 'png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        plt.close()
        context = {
            'data' : uri
        }
        return render(request,'customers/future.html',context)
    else:
        
        return render(request,'customers/sorry.html')


###########################################################################################################

@login_required(login_url='shop_login')
def growth(request):
    shops = request.user.username
    all_data = data.objects.all().filter(shop=shops).values()
    all_data = pd.DataFrame(all_data)
    all_data['Order_Date'] = pd.to_datetime(all_data['Order_Date'],  errors='coerce', format ='%m/%d/%Y %H:%M')
    all_data['Month'] = pd.to_datetime(all_data['Order_Date']).dt.year
    all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
    all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
    all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
    all_data = all_data.groupby(['Month']).sum()['Sales']
    all_data['Revenue Growth'] = all_data.pct_change()
    print(all_data['Revenue Growth'])

    return render(request,'customers/sam.html')
    
    
@login_required(login_url='shop_login')
def top(request):
    shops = request.user.username
    all_data = data.objects.all().filter(shop=shops).values()
    all_data = pd.DataFrame(all_data)
    all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
    all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
    all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
    # Grouping products by Quantity
    best_selling_prods = pd.DataFrame(all_data.groupby('Product').sum()['Quantity'])

    # Sorting the dataframe in descending order
    best_selling_prods.sort_values(by=['Quantity'], inplace=True, ascending=False)

    # Most selling products
    p = best_selling_prods[:10]
    

    return render(request,'customers/top.html',{'p': p.to_html() })

def traffic(request):
    all_data = data.objects.all().values()
    all_data = pd.DataFrame(all_data)
    all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
    all = all_data['Quantity'].sum()
    print(all)

    all_data['Order_Date'] = pd.to_datetime(all_data['Order_Date'],  errors='coerce', format ='%m/%d/%Y %H:%M')
    all_data['Month'] = pd.to_datetime(all_data['Order_Date']).dt.year==2021

    all_data['Quantity'] = pd.to_numeric(all_data['Quantity'])
    all_data['Price_Each'] = pd.to_numeric(all_data['Price_Each'])
    all_data['Sales'] = all_data['Quantity'].astype('int') * all_data['Price_Each'].astype('float')
    all_data['Month'] = pd.to_datetime(all_data['Order_Date']).dt.year==2021
    all_data = all_data.groupby(['Month']).sum()
    
    a= all_data['Sales'].filter(['Month',True])
    # b = a.filter(['Month',True])
    print(a)
    # if all_data.bool()==T:
    #     #all_data = all_data.groupby(['Month']).sum()
    #     all_data = all_data['Sales'].sum()
    #     print(all_data)
    return render(request,'customers/sam.html')

@login_required(login_url='shop_login')
def stat(request):
    a=get_object_or_404(Order, pk=request.GET.get('id'))
    a.status=True
    a.save()
    return redirect(reverse('ordered_list'))

@login_required(login_url='shop_login')
def delete(request):
    a=get_object_or_404(Order, pk=request.GET.get('id'))
    a.delete()
    return redirect(reverse('ordered_list'))

#######################################################################################################
from PIL import Image,ImageEnhance
import pytesseract
import cv2
import numpy as np
from service.models import Comp
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
@login_required(login_url='shop_login')
def uploadd(request):
    cus = request.user
    if request.method == 'POST':
        
        
        if 'file' not in request.FILES:
            return render(request,'customers/uploadd.html')
        file = request.FILES['file']
        
        extracted_text = ocr_core(file)
        scan = Comp(image= file,snum=extracted_text,cus_id=cus)
        scan.save()
        #txt = extracted_text.split()
        
        return render(request,'customers/uploadd.html',
                                   {'extracted_text':extracted_text},
                                   )
        
    elif request.method == 'GET':
        return render(request,'customers/uploadd.html')

@login_required(login_url='shop_login')
def View_data(request):
    id = request.user
    s = Comp.objects.all().filter(cus_id_id = id)
    return render(request,'customers/view_data.html',{'s':s})
