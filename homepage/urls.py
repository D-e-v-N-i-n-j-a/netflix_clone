from . import views
from django.urls import path



urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('views/<str:pk>',views.view,name='view') 
]






