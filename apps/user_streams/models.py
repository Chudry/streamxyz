from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class StreamModel(models.Model):
    """ stream is like a channel/broadcast,
        where users shares information frequently """
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='stream', max_length=300)
    description = models.TextField(default='')
    keywords = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='user_streams')
    private = models.BooleanField(default=False)
    blacklist = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(StreamModel, self).save(*args, **kwargs)


    def __str__(self):
        return '%s [%s]' % (self.name, self.author)

    class Meta:
        db_table = 'stream'
        verbose_name = 'Stream'
        verbose_name_plural = 'Streams'
        ordering = ['-views']


class StreamItemModel(models.Model):
    """ stream item/post """
    stream = models.ForeignKey(StreamModel)
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    keywords = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    video_url = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, related_name='user_stream_items')
    blacklist = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.url:
            if '//youtube.' in self.url or '.youtube.' in self.url:
                self.video_url = self.url.replace("watch?v=", "embed/")
        super(StreamItemModel, self).save(*args, **kwargs)

    def __str__(self):
        return '%s [%s]' % (self.title, self.author)

    class Meta:
        db_table = 'stream_item'
        verbose_name = 'Stream Item'
        verbose_name_plural = 'Stream Items'
        ordering = ['-created_on']
