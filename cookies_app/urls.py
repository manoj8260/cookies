from django.urls import path
from .views import   * 
urlpatterns =[
    path('set/',set_cookies,) ,
    path('get/',get_cookies,) ,
    path('del/',del_cookies,) , 
    path('setsigned/',setsigned_cookies,) , 
    path('getsigned/',getsined_cookies,) , 
   
]