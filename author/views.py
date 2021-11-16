from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
from django.views.generic import ListView,CreateView


# Create your views here.

def AuthorAdd(request):
    a1 = Author.objects.create(auth_name="Hani" , bio="Bio of Auther 1")
    return HttpResponse('added')    


def AuthorList(request):
    viewall = Author.objects.all()
    return HttpResponse(viewall)


class AuthorListGen(ListView):
    model = Author


def index(request):
    return render(request,'author/index.html')


class AuthorCreateView(CreateView):
    model = Author


# def DelAuthor(request,auth_name):
#     Author.objects.filter(auth_name=auth_name).delete()
#     return HttpResponse('Deleted')