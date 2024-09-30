from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, app_two!")


def catalog(request):
    return HttpResponse("Hello, app_two catalog!")


def news(request):
    return HttpResponse("Hello, app_two news!")
