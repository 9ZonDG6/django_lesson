from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, app_one!")


def catalog(request):
    return HttpResponse("Hello, app_one catalog!")


def news(request):
    return HttpResponse("Hello, app_one news!")
