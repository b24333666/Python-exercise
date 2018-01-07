from django.http import HttpResponse


def home(request):
    s = "Hello World!!"
    return HttpResponse(s)