from typing import Reversible
from django.shortcuts import redirect, render
from author.models import Author
from .models import Book
from django.http import HttpResponse
from .forms import AddBookForm,BookUpdateForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.db import models
from django.views.generic import ListView 


def BookList(request):
    booklist = Book.objects.all()
    context = {'booklist': booklist }
    return render(request, 'book/booklist.html', context)

def BookAdd(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # main url :: secondary url
            return redirect('booklist')
        pass
    else:
        form = AddBookForm()
    return render(request, 'book/bookadd.html', {'form': form})

def BookUpdate(request,bid):
    book = Book.objects.get(bid=bid)
    print(book)
    form = BookUpdateForm(request.POST or None ,instance= book)
    if form.is_valid():
        form.save()
        return redirect('booklist')
    return render(request, 'book/bookedit.html', {'form': form})
    
def BookDelete(request,bid):
    book = Book.objects.get(bid=bid).delete()
    return redirect('booklist')
    