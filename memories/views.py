from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required
from authorization.get_profile import UserInfoGetter
from authorization.decorators import login_required_with_message

from .forms import Memory, MemoryForm


def index(request):
    return render(request, 'index.html')


@login_required_with_message
def delete_memory(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    if memory.user != request.user:
        return redirect(home)
    memory.delete()
    return redirect(home)


@login_required_with_message
def home(request):
    user_profile = UserSocialAuth.objects.get(user=request.user)
    access_token = user_profile.access_token
    userinfo_getter = UserInfoGetter(access_token)

    if user_profile.provider == 'vk-oauth2':
        pers_id, first_name, last_name, photo_url = userinfo_getter.get_vk_info()
    elif user_profile.provider == 'google-oauth2':
        pers_id, first_name, last_name, photo_url = userinfo_getter.get_google_info()
    else:
        return HttpResponse('Авторизации нет')

    memories = Memory.objects.filter(user=request.user)

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'photo_url': photo_url,
        'memories': memories,
    }
    return render(request, 'home.html', context)


@login_required_with_message
def create_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')

            if latitude is None or longitude is None or latitude == '' or longitude == '':
                error_message = 'Выберите точку на карте.'
                return render(request, 'сreate_memory.html', {'form': form, 'error_message': error_message})

            memory.latitude = latitude
            memory.longitude = longitude
            memory.save()
            return redirect(home)
    else:
        form = MemoryForm()

    return render(request, 'сreate_memory.html', {'form': form})


@login_required_with_message
def logout(request):
    auth.logout(request)
    return redirect(index)
