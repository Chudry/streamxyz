from django.shortcuts import render

# Create your views here.
from django.views import View

from user_streams.models import StreamModel
from user_collections.models import CollectionModel


class HomeView(View):

    def get(self, request):
        context = {
            'streams': StreamModel.objects.all()[0:10],
            'collections': CollectionModel.objects.all()[0:10],
        }
        return render(request, 'core/home.html', context)
