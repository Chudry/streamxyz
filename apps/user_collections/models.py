from django.db import models
from django.contrib.auth.models import User


class CollectionModel(models.Model):
    """ collection is like a place where user stores his favorite items
    """
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='user_collections')
    private = models.BooleanField(default=False)
    blacklist = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return '%s [%s]' % (self.name, self.author)

    class Meta:
        db_table = 'collection'
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'


class CollectionItemModel(models.Model):
    """ collection item/post """
    collection = models.ForeignKey(CollectionModel)
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    url = models.TextField()
    author = models.ForeignKey(User, related_name='user_collection_items')
    blacklist = models.BooleanField(default=False)
    video_url = models.TextField(null=True, blank=True)
    order_index = models.IntegerField(default=0)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        if self.url:
            if '//youtube.' in self.url or '.youtube.' in self.url:
                self.video_url = self.url.replace("watch?v=", "embed/")
        super(CollectionItemModel, self).save(*args, **kwargs)

    def __str__(self):
        return '%s [%s]' % (self.title, self.author)

    class Meta:
        db_table = 'collection_item'
        verbose_name = 'Collection Item'
        verbose_name_plural = 'Collection Items'
