from django.shortcuts import render

# Create your views here.

def set_cookies(request):
    response = render(request,'setcookies.html')
    return response
def get_cookies(request):
    response = render(request,'getcookies.html')
    return response
def del_cookies(request):
    response = render(request,'delcookies.html')
    return response