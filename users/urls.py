"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from users.views import CreationView, AuthView, DetailsView
import django
from src import settings

urlpatterns = [
    url(r'^fb_login_or_create?$', CreationView.as_view()),
    url(r'^create_customer?$', CreationView.as_view()),
    url(r'^create_driver?$', CreationView.as_view()),
    url(r'^get_driver_details?$', DetailsView.as_view()),
    url(r'^login?$', AuthView.as_view()),
    url(r'^logout?$', AuthView.as_view()),
    url(r'^add_profile_pic$', DetailsView.as_view()),
    url(r'^media/(profilepics/.*)$', django.views.static.serve,{'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),

]