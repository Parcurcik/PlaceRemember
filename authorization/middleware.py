from django.shortcuts import redirect, render
from django.contrib import messages

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path == '/home/':
            messages.error(request, 'Пожалуйста, авторизуйтесь')
            return redirect('/')
        response = self.get_response(request)
        return response
