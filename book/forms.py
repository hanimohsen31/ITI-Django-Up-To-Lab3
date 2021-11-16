from django import forms
from django.db import models
from django.forms.models import model_to_dict

from author.models import Author
from .models import Book
from django import forms


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','category']
