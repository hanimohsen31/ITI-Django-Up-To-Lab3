from django.urls import path
from author import views as authorview
from.views import index,AuthorListGen,AuthorCreateView

urlpatterns = [
    path('adda', authorview.AuthorAdd),
    path('lista', authorview.AuthorList),
    path('lgen',AuthorListGen.as_view()),
    path('lgenc',AuthorCreateView.as_view()),
]
