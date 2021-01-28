from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 57d2108c is the polls index.")
