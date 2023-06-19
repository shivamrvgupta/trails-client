from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from custom.models import Customs
# Create your views here.
def customs(request):
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
        
