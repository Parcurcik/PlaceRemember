from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required
from authorization.get_profile import UserInfoGetter


def index(request):
    return render(request, 'index.html')


@login_required
def home(request):
    return render(request, 'home.html')


def vk_callback(request):
    try:
        vk_user = UserSocialAuth.objects.get(provider='vk-oauth2', user=request.user)
        vk_profile = vk_user.extra_data
        user_info = UserInfoGetter(vk_profile['access_token'])
        name, last_name, photo = user_info.get_vk_info()
        print(name, last_name, photo, sep='\n')
    except UserSocialAuth.DoesNotExist:
        pass
    return redirect(home)


def google_callback(request):
    try:
        user_social_auth = UserSocialAuth.objects.get(provider='google-oauth2', user=request.user)
        user_info = user_social_auth.extra_data
        user_info = UserInfoGetter(user_info['access_token'])
        name, last_name, photo = user_info.get_google_info()
        print(name, last_name, photo, sep='\n')
    except UserSocialAuth.DoesNotExist:
        pass
    return redirect(home)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(index)
