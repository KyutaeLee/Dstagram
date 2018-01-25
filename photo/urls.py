from django.conf.urls import url
from . import views
# 한가지 골라서 import 하려면
#from .views import post_list
from django.views.generic import DetailView
# 장고에서 미리 만들어 놓은
from .models import Photo
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^single/(?P<pk>\d+/$', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='post_detail'),
    #localhost:8000/photo/single/123/


]
