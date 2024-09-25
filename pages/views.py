from django.http import HttpResponse


def homePageView(request):
    """HomePageView"""
    return HttpResponse("Hello World")
