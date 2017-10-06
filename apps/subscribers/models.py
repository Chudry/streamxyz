from django.db import models


class SubscriberModel(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=255)
    interest = models.CharField(max_length=255)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subscriber'
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return '%s' % self.email
