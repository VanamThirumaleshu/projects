from django.urls import path
from . import views


urlpatterns=[
    path('',views.details),
    path('details/',views.showdetails,name='details'),
    
]