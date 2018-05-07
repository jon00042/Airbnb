from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('login_ajax', views.login_ajax, name='login_ajax'),
    path('signup_ajax', views.signup_ajax, name='signup_ajax'),
] + static('/media', document_root=settings.BASE_DIR + '/media')

