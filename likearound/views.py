from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import models
from . import forms
import json

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

@login_required
@csrf_exempt
def like(request, *args, **kwargs):
    response = {}
    if request.method in 'POST':
        req = json.loads(request.body)['params']
        liker = models.Profile.objects.get(user=request.user)
        likee = models.Profile.objects.get(pk=req.get('id'))
        sign = req.get('sign')
        likee.like(liker, is_positive=sign)
        response['likes'] = likee.likes
        response['dislikes'] = likee.dislikes
        response['liked'] = likee.liked(liker)
    return HttpResponse(
        json.dumps(response),
        content_type="application/json"
    )

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

