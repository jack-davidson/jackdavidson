from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blogid>', views.blog, name='blog'),
]
