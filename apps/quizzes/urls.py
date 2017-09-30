from django.conf.urls import url

from django.views.generic import TemplateView
from . import views


# Non API Urls
urlpatterns = [

    url(r'^$', views.QuizList.as_view()),
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[-\w]+)/$', views.QuizDetail.as_view()),

]
