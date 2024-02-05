

from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('service/',service,name='service'),
    path('register/',register,name='register'),
    path("registerdata/",UserRegister,name="registerdata"),
    path('login/',login,name='login'),
    path('loginUser/',loginUser,name='loginUser'),
    path("query/<str:pk>",query,name="query"),
    path('showpage/<str:pk>',showdata,name='showdata'),
    path('editpage/<int:pk>/',editPage,name='editpage'),
    path('update/<int:pk>/',updateData,name='update'),
    path('delete/<int:pk>/',deleteData,name='delete'),
    
    
    
    
]