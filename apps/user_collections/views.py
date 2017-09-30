
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.core.cache import cache


from user_collections.models import CollectionModel, CollectionItemModel


class CollectionList(View):

    def get(self, request):
        context = {
            'collections': CollectionModel.objects.filter(
                private=False, blacklist=False)[0:50]
        }
        return render(request, 'user_collections/list.html', context)


class CollectionDetail(View):

    def get(self, request, pk, slug):
        collection = CollectionModel.objects.get(id=pk)
        items = CollectionItemModel.objects.filter(
            collection=collection, blacklist=False)

        client_address = request.META.get('REMOTE_ADDR', None)
        if client_address:
            hit_key = '%s-%s-%s' % (client_address, 'collection', collection.id)
            if cache.get(hit_key, None) is None:
                collection.views = collection.views + 1
                collection.save()
                cache.set(hit_key, '1', 60*60*1)  # 1 hour

        context = {
            'collection': collection,
            'items': items
        }

        return render(request, 'user_collections/detail.html', context)
