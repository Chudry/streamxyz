from django.conf.urls import url

from django.views.generic import TemplateView
from . import views


# Non API Urls
urlpatterns = [

    url(r'^$', views.HomeView.as_view()),
    url(r'^about/$',
        TemplateView.as_view(template_name="core/about.html")),

]


# API Urls
urlpatterns += []
