from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, Product
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.

@login_required(login_url='/accounts/login')
def cart(request):
    lists = Cart.objects.order_by('-modified_date')
    context = {
        'lists': lists
    }

    return render(request, 'products/cart.html',context)



def listings(request):
    listings = Product.objects.order_by('-list_date').filter(is_published=True)
    add = int(1)
    
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = request.POST['user']
        product = request.POST['product']
        quantity = request.POST['quantity']
        price = request.POST['price']
        small_photo = request.POST['small_photo']
        print("user sweep")
        print(f"-------- {user}{product}")

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Cart.objects.all().filter(user=user, product=product,quantity=quantity,price=price,small_photo=small_photo)
            print("New Enquiry Sent ")
            if has_contacted:
                quantity = quantity + str(1)
                print("peep")
                return redirect('cart')

        cart = Cart(user=user, product=product,quantity=quantity,price=price,small_photo=small_photo)
        cart.save()
        print("Request Saved")
        return redirect('cart')

    context = {
        'listings': listings
    }
    return render(request, 'products/listings.html', context)


def delete_data(request, id):
    if request.method == 'POST':
        result = Cart.objects.get(pk=id)
        result.delete()
        return HttpResponseRedirect('/')
    


