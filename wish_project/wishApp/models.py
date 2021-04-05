from django.db import models

# Create your models here.
class Wish(models.Model):
    text = models.TextField(blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Subscribers(models.Model):
    msisdn = models.CharField(max_length=13, blank=False, unique=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.msisdn


class Requests(models.Model):
    sender_subs_id = models.ForeignKey(Subscribers, on_delete=models.DO_NOTHING, related_name='sender_subs_id')
    recipient_subs_id = models.ForeignKey(Subscribers, on_delete=models.DO_NOTHING, related_name='recipient_subs_id')
    wish = models. ForeignKey(Wish, on_delete=models.DO_NOTHING)
    add_date = models.DateTimeField(auto_now_add=True)
    gifts = models.ManyToManyField('Gifts')


class Gifts(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.FloatField(default=0, null=False)


class Request_gifts(models.Model):
    gift_id = models.ForeignKey(Gifts, on_delete=models.DO_NOTHING)
    request_id = models.ForeignKey(Requests, on_delete=models.DO_NOTHING)





