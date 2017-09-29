from django.db import models
from django.contrib.auth.models import User


class StreamModel(models.Model):
    """ stream is like a channel/broadcast,
        where users shares information frequently """
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='user_streams')
    private = models.BooleanField(default=False)
    blacklist = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return '%s [%s]' % (self.name, self.author)

    class Meta:
        db_table = 'stream'
        verbose_name = 'Stream'
        verbose_name_plural = 'Streams'


class StreamItemModel(models.Model):
    """ stream item/post """
    stream = models.ForeignKey(StreamModel)
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    url = models.TextField()
    author = models.ForeignKey(User, related_name='user_stream_items')
    blacklist = models.BooleanField(default=False)

    def __str__(self):
        return '%s [%s]' % (self.title, self.author)

    class Meta:
        db_table = 'stream_item'
        verbose_name = 'Stream Item'
        verbose_name_plural = 'Stream Items'
