from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required 
#to check if somebody is logged in or not
#just add @login_required above the function

from . import models

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Creation Successful.Please login to continue!')
            return redirect('login') #using url name

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})



