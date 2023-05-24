from pyexpat import model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_models

# Create your models here.


class News(models.Model):
    
    # information
    image = models.ImageField('Şəkil', upload_to = 'media/news')
    title = models.CharField('Başlıq', max_length = 256)
    description = tinymce_models.HTMLField('Qısa məzmun', max_length = 10000)
    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)
    
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_details', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while News.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(News, self).save(*args, **kwargs)


class Programs(models.Model):

    # information
    image = models.ImageField('Şəkil', upload_to = 'media/programs')
    other_image1 = models.ImageField('Əlavə Şəkil 1', upload_to = 'media/programs', null=True, blank=True)
    other_image2 = models.ImageField('Əlavə Şəkil 2', upload_to = 'media/programs', null=True, blank=True)
    other_image3 = models.ImageField('Əlavə Şəkil 3', upload_to = 'media/programs', null=True, blank=True)
    title = models.CharField('Başlıq', max_length = 256)
    description = tinymce_models.HTMLField('Qısa məzmun', max_length = 10000)
    time = models.CharField('Deadline:', max_length = 256)
    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)
    is_published = models.BooleanField('is published', default=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('programs_details', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while Programs.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(Programs, self).save(*args, **kwargs)


class Event(models.Model):

    # information
    image = models.ImageField('Şəkil', upload_to = 'media/events')
    other_image1 = models.ImageField('Əlavə Şəkil 1', upload_to = 'media/events', null=True, blank=True)
    other_image2 = models.ImageField('Əlavə Şəkil 2', upload_to = 'media/events', null=True, blank=True)
    other_image3 = models.ImageField('Əlavə Şəkil 3', upload_to = 'media/events', null=True, blank=True)
    title = models.CharField('Başlıq', max_length = 256)
    location = models.CharField('Ünvan', max_length = 256)
    description = tinymce_models.HTMLField('Qısa məzmun', max_length = 10000)
    time = models.CharField('Zaman', max_length = 256)
    slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)
    is_published = models.BooleanField('is published', default=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_details', kwargs = {'slug': self.slug})

    def get_uniqe_slug(self):
        slug = slugify(self.title.replace('ə', 'e'))
        unique_slug = slug
        counter = 1
        while Event.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_uniqe_slug()
        return super(Event, self).save(*args, **kwargs)