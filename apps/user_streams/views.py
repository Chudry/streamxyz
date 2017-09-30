
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.core.cache import cache


from user_streams.models import StreamModel, StreamItemModel


class StreamList(View):

    def get(self, request):
        context = {
            'streams': StreamModel.objects.filter(
                private=False, blacklist=False)[0:50]
        }
        return render(request, 'user_streams/list.html', context)


class StreamDetail(View):

    def get(self, request, pk, slug):
        stream = StreamModel.objects.get(id=pk)
        items = StreamItemModel.objects.filter(
            stream=stream, blacklist=False)

        client_address = request.META.get('REMOTE_ADDR', None)
        if client_address:
            hit_key = '%s-%s-%s' % (client_address, 'stream', stream.id)
            if cache.get(hit_key, None) is None:
                stream.views = stream.views + 1
                stream.save()
                cache.set(hit_key, '1', 60*60*1)  # 1 hour

        context = {
            'stream': stream,
            'items': items
        }

        return render(request, 'user_streams/detail.html', context)
