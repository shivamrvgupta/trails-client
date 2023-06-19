from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from blogs.models import Blog,Newsletter
from custom.models import Customs
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse


# Create your views here.

def index(request):
    listings = Product.objects.order_by('-list_date').filter(is_published=True)
    blogs = Blog.objects.order_by('-date').filter(is_published=True)
    
    context = {
        'listings' : listings,
        'blogs' : blogs,
    }
    return render(request, 'pages/index.html',context)

def trying(request):
    return render(request, 'pages/trying.html')
        
def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        print('Enquiry Checking ---')

        contact = Newsletter(email=email)           
        print("Request been checked")
        contact.save()
        print("Request Saved")
        send_mail(
            'Thank You For Subscribing',
            'Hello Sir/Madam, thank you for subscribing. You will revicing the updates from know onwards',
            'shivamrvgupta@gmail.com',
            [email,'rvshivamsahu.1222@gmail.com'],
            fail_silently=False,
        )
        return HttpResponseRedirect('/')

"""def customs(request):
    if request.method == 'POST':
        # Get form value
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        desc = request.POST['desc']
        refimg = request.POST['refimg']

    context ={
        'customs' : customs
    }
    return render(request, 'pages/customs.html')

def about(request):
    return render(request, 'pages/about.html')"""