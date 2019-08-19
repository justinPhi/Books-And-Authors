from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^addbook$', views.addBook),
        url(r'^showbook/(?P<val>\d+)$', views.showBook),
        url(r'^addauthortobook', views.addAuthorToBook),

        ]

