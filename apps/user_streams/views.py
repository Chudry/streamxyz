
from django.shortcuts import render

# Create your views here.
from django.views import View


from user_streams.models import StreamModel, StreamItemModel


class StreamList(View):

    def get(self, request):
        context = {
            'streams': StreamModel.objects.filter(
                private=False, blacklist=False)[0:50]
        }
        return render(request, 'user_streams/list.html', context)


class StreamDetail(View):

    def get(self, request, pk):
        stream = StreamModel.objects.get(id=pk)
        items = StreamItemModel.objects.filter(
            stream=stream, blacklist=False)
        context = {
            'stream': stream,
            'items': items
        }
        return render(request, 'user_streams/detail.html', context)
