from django.db import models

from distutils.command.upload import upload
from operator import mod
from turtle import update
from django.db import models
from accounts.models import Account
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from uuid import uuid4
from django.utils.text import slugify
import random as r

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'news_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path



class TestSlugModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return str(self.title)
    
@receiver(post_delete, sender=TestSlugModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(pre_save, sender=TestSlugModel)
def pre_save_compl_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))

