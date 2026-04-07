from django.http import JsonResponse


def root(request):
    return JsonResponse({
        'admin': '/admin/',
        'register': '/api/auth/register/',
        'login': '/api/auth/login/',
        'refresh': '/api/auth/refresh/',
        'logout': '/api/auth/logout/',
    })
