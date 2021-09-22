from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from datetime import datetime

from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

    crew_choices = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('solo', 'solo'),
    )

    camera_choices = (
        ('sony', 'sony'),
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('panasonic', 'panasonic'),
        ('red', 'red'),
        ('fuji', 'fuji'),
        ('other', 'other'),
    )

    category_choices = (
        ('Tech', 'Tech'),
        ('Vloggers', 'Vloggers'),
        ('Music', 'Music'),
        ('Mobile_Unboxing', 'Mobile_Unboxing'),
        ('Comedy', 'Comedy'),
        ('Gaming', 'Gaming'),
        ('Cooking', 'Cooking'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField(choices = crew_choices, max_length=255)
    camera_type = models.CharField(choices = camera_choices,  max_length=255)
    subs_count = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    category = models.CharField(choices = category_choices, max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name