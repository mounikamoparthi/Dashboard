from django.conf.urls import url
from . import views        
app_name = 'travels'   
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
   
    url(r'^addtrip$', views.addtrip , name ='addtrip'),
    #url(r'^showtrip/(?P<id>\d+)$', views.showtrip , name ='showtrip') ,
  ]