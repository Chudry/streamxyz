from django.conf.urls import url

from django.views.generic import TemplateView
from . import views


# Non API Urls
urlpatterns = [

    url(r'^$', views.CollectionList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CollectionDetail.as_view()),

]
