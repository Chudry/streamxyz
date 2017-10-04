from django.shortcuts import render

# Create your views here.
from django.views import View

from user_streams.models import StreamModel
from user_collections.models import CollectionModel
from quizzes.models import QuizModel


class HomeView(View):

    def get(self, request):
        context = {
            'streams': StreamModel.objects.filter(private=False, blacklist=False)[0:10],
            'collections': CollectionModel.objects.filter(private=False, blacklist=False)[0:10],
            'quizzes': QuizModel.objects.filter(private=False, blacklist=False)[0:10]
        }
        return render(request, 'core/home.html', context)
