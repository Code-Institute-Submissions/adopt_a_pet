from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('pets')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form })

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form })