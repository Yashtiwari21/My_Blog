from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("forms/", views.forms, name="forms"),
    path("submit/", views.submit, name="submit"),
    path("about/", views.about, name="blog-about"),
]
