from django.contrib import messages
from django.contrib.auth.decorators import login_required
from functools import wraps

from django.shortcuts import redirect


def login_required_with_message(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Пожалуйста, авторизуйтесь')
            return redirect('/')
        return login_required(function)(request, *args, **kwargs)

    return wrapper
