from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View
from customer.models import shop_user
from store.models.customer import Customer

# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    #if request.method == 'POST': 
    prod = request.POST.get('searched')  
        
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    elif prod:
        products = Products.objects.filter(name=prod)
    else:
        products = Products.get_all_products();
    #-------------------------------------------------------------------
    finds = shop_user.objects.all()
    customer = request.session.get('customer')
    cus = Customer.objects.all()
    #for i in cus:
        #f=i.id
        #if (customer==f):
            #p = i.pincode
            #print(p)
        
    #-------------------------------------------------------------------
    data = {}
    data['products'] = products
    data['categories'] = categories
    data['finds'] = finds
    #data['f']= f
    data['customer'] = customer
    data['cus']=cus
    
    print('you are : ', request.session.get('customer'))
    return render(request, 'index.html', data)



