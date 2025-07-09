from django.shortcuts import render
from datetime import datetime ,timezone ,timedelta
# Create your views here.

def set_cookies(request):
    response = render(request,'setcookies.html')
    response.set_cookie('token','token7732218',max_age=3600)
    response.set_cookie('payid','payid111111',expires=datetime.now(timezone.utc)+(timedelta(days=2)))
    return response
def get_cookies(request):
    cookies = request.COOKIES.get('token')
    response = render(request,'getcookies.html' ,{'cookies' : cookies})
    return response
def del_cookies(request):
    response = render(request,'delcookies.html')
    response.delete_cookie('token')
    return response

def setsigned_cookies(request):
    response = render(request,'setsignedcookies.html')
    response.set_signed_cookie('s_token' , 'stoken123577' ,salt='stk')
    return  response
def getsined_cookies(request):
    token = request.get_signed_cookie('s_token',salt = 'stk',default ='defaulttoken-1345')
    response = render(request,'getsinedcookies.html' , {'token' :token})
    return  response