from django.conf.urls import url 
from . import views 

urlpatterns = [
    url(r'^$', views.home),
    url(r'^add_contact$', views.add_contact), 
    url(r'^display_ssot$', views.display_ssot), 
    url(r'^submit_ssot$', views.submit_ssot),
    url(r'^display_winter_jubilee$', views.display_winter_jubilee), 
    url(r'^submit_winter_jubilee$', views.submit_winter_jubilee),
    url(r'^home_meetings$', views.home_meetings), 
    url(r'^announcements$', views.announcements), 
    url(r'^post_announcement', views.post_announcement), 

]

