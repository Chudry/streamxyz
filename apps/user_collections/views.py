
from django.shortcuts import render

# Create your views here.
from django.views import View


from user_collections.models import CollectionModel, CollectionItemModel


class CollectionList(View):

    def get(self, request):
        context = {
            'collections': CollectionModel.objects.filter(
                private=False, blacklist=False)[0:50]
        }
        return render(request, 'user_collections/list.html', context)


class CollectionDetail(View):

    def get(self, request, pk):
        collection = CollectionModel.objects.get(id=pk)
        items = CollectionItemModel.objects.filter(
            collection=collection, blacklist=False)
        context = {
            'collection': collection,
            'items': items
        }
        return render(request, 'user_collections/detail.html', context)
