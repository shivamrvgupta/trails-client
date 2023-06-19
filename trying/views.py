from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from trying.models import Trying
# Create your views here.
def trying(request):
    if request.method == 'POST':
        # Get form value
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        desc = request.POST['desc']
        refimg = request.POST['refimg']
        
    return render(request, 'pages/try.html')
        
