from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('signup_ajax', views.signup_ajax, name='signup_ajax'),
]

