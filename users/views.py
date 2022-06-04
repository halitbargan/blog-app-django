from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def user_login(request):
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            
            login(request,user)
        return redirect ('home')
    return render (request, 'user/user_login.html', {'form':form})