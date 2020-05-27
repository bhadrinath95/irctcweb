from django import forms
from django.forms import formset_factory
from .models import Book
from django.forms import modelformset_factory

BookModelFormset = modelformset_factory(
    Book,
    fields=('name', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    }
)