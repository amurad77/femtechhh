
# from click import Choice
from django import forms
from .models import Contact, Involved
from django.utils.translation import gettext as _
from django.forms import ModelForm, Select, TextInput


FORM_CHOICES= [
    ('1', 'Become *'),
    ('2', 'Speaker'),
    ('3', 'Partner'),
    ('4', 'Member'),
    ]



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'number',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Name',
                                    'type': 'text'
                                    
                                }),
            'email': forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Email',
                                    'type': 'email'
                                    
                                }),
            'number': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Phone',
                                    'type': 'text'
                                }),
            'message': forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Message',
                                    'cols': 30,
                                    'rows': 8,

                                })
        }



class InvolvedForm(forms.ModelForm):

    class Meta:
        model = Involved
        fields = (
            'name',
            'email',
            'number',
            'membership_type',
            'message',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Name *',
                                    'type': 'text'
                                    
                                }),
            'email': forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'E-mail Address *',
                                    'type': 'email'
                                    
                                }),
            'number': forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Phone Number *',
                                    'type': 'text'
                                }),
            'membership_type': Select(attrs={
                                    'class': 'form-control',
                                }),
            'message': forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Motivation for being with us…',
                                    # 'cols': 30,
                                    # 'rows': 8,

                                })
        }