from django.http import JsonResponse


def root(request):
    return JsonResponse({
        'admin': '/admin/',
        'token': '/api/token/',
        'refresh': '/api/token/refresh/',
    })
