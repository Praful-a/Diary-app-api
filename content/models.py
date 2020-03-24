from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=50, null=True)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = 'entries'


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=Entry)
