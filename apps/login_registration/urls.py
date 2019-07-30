from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^display_login_registration$', views.display_login_registration),
    url(r'^register$', views.register), 
    url(r'^login$', views.login),
]

