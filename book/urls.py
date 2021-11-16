from django.contrib import admin
from django.urls import include, path
from . import views 


urlpatterns = [
    path('', views.BookList),
    path('addbook', views.BookAdd,name='addbook'),
    path('booklist', views.BookList,name='booklist'),
    path('update/<int:bid>', views.BookUpdate,name='update'),
    path('delete/<int:bid>', views.BookDelete,name='delete'),
]