# from ast import Param
# from distutils import core
# from email import message
# from http import client
# from unicodedata import name
# from turtle import title
from email.policy import default
from random import choices
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce import models as tinymce_models



# Create your models here.

MODEL_CHOICES= [
    ('1', 'Become *'),
    ('2', 'Speaker'),
    ('3', 'Partner'),
    ('4', 'Member'),
    ]


class Involved(models.Model):
    
    # information
    name = models.CharField('Ad', max_length = 256)
    email = models.EmailField('Email', max_length = 50)
    number = models.CharField('Telefon nömrəsi', max_length = 20)
    membership_type = models.CharField('Membership type', choices = MODEL_CHOICES, default = 'Become *', max_length = 256)
    message = models.TextField('Mesaj', max_length = 2000)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    
    # information
    name = models.CharField('Ad', max_length = 256)
    email = models.EmailField('Email', max_length = 50)
    number = models.CharField('Telefon nömrəsi', max_length = 20)
    message = models.TextField('Mesaj', max_length = 2000)
    
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.name


class Team(models.Model):

    # information
    name = models.CharField('Ad', max_length = 256)
    image = models.ImageField('Şəkil', upload_to = 'media/team')
    positions = models.CharField('Vəzifə', max_length = 256)
    email = models.EmailField('Email', max_length = 50, null=True, blank=True)
    linkedin_link = models.CharField('Linkedin link', max_length = 200)
    
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Alumnis(models.Model):

    # information
    name = models.CharField('Ad', max_length = 256)
    image = models.ImageField('Şəkil', upload_to = 'media/team')
    program = models.CharField('İştirak etdiyi program', max_length = 256)
    
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Program(models.Model):
#     name = models.CharField('Ad', max_length = 256)
#     description = tinymce_models.HTMLField('Qısa məzmun', max_length = 10000)
#     image = models.ImageField('Şəkil', upload_to = 'media/program')
#     slug = models.SlugField('Slug', max_length = 110, unique = True, editable = False)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('alumnis', kwargs = {'slug': self.slug})

#     def get_uniqe_slug(self):
#         slug = slugify(self.name.replace('ə', 'e'))
#         unique_slug = slug
#         counter = 1
#         while Program.objects.filter(slug = unique_slug).exists():
#             unique_slug = '{}-{}'.format(slug, counter)
#             counter += 1
#         return unique_slug

#     def save(self, *args, **kwargs):
#         self.slug = self.get_uniqe_slug()
#         return super(Program, self).save(*args, **kwargs)


# class Alumnis(models.Model):
#     #relation's
#     program = models.ForeignKey(Program, on_delete = models.CASCADE)

#     name = models.CharField('Ad', max_length = 256)
#     image = models.ImageField('Şəkil', upload_to = 'media/aulmnis')

#     # moderations
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Partners(models.Model):
    image = models.ImageField('Logo', upload_to = 'media/partners')

    # def __str__(self):
    #     return self.image

class Statitics(models.Model):
    events = models.IntegerField('Events', default = 0)
    members = models.IntegerField('Members', default = 0)
    collaborations = models.IntegerField('Collaborations', default = 0)
    participants = models.IntegerField('Participants', default = 0)
    initiatives = models.IntegerField('Initiatives', default = 0)
