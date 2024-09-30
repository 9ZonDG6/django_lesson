from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, app_three!")


def catalog(request):
    return HttpResponse("Hello, app_three catalog!")


def news(request):
    return HttpResponse("Hello, app_three news!")
