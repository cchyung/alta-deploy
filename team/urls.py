from django.conf.urls import url

from . import views

app_name = 'team'
urlpatterns = [
    url(r'(?P<slug>([a-z]|-)+)/$', views.detail, name='detail'),
]