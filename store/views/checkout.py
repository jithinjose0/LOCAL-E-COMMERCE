from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from customer.models import shop_user
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        #shops = shop_user.get_shop_by_id(list(cart.keys()))
        #print(address, phone, customer, cart, products,shops)
        #print("shooooooooooopppppppppppppppppppppppp===========",shops)
        
        for product in products:
            #for shop in shops:

            print(cart.get(str(product.id)))
            #print(cart.get(str(shop.id)))
            p=product.shops
            order = Order(customer=Customer(id=customer),
                    product=product,
                    shopss=p.username,
                    price=product.price,
                    address=address,
                    phone=phone,
                    quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
