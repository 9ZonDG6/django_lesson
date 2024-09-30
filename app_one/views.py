from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, first app!")


def catalog(request):
    return HttpResponse("Hello, app_one catalog!")


def news(request):
    return HttpResponse("Hello, app_one news!")
