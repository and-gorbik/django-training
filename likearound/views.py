from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from . import models
from . import forms

def profiles(request, *args, **kwargs):
    context = {
        'profiles': models.Profile.objects.all()
    }
    return render(request, 'likearound/profiles.html', context)

def profile(request, pk, *args, **kwargs):
    context = {
        'profile': models.Profile.objects.get(user=pk)
    }
    return render(request, 'likearound/profile.html', context)

def signup(request, *args, **kwargs):
    form = forms.UserCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('profiles')
    return render(request, 'likearound/signup.html', {'form': form})

def signout(request, *args, **kwargs):
    logout(request)
    return redirect('index')

def signin(request, *args, **kwargs):
    print('\nhere\n')
    form = forms.UserLoginForm(request.POST)
    if 'login' in request.POST:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = get_user_model().objects.get(username=username)
            login(request, user)
            print('\nlogin\n')
            
    return redirect('index')

# class SignUpUser():
#     pass

# class SignInUser():
#     pass

# class SignOutUser():
#     pass

# class ProfileView():
#     pass

# class ProfileDetail():
#     pass

