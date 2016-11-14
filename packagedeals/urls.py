from django.conf.urls import include, url
from django.contrib import admin
import django
from views import PackagedealView

from src import settings
urlpatterns = [
	
    url(r'^create_packagedeal/?$', PackagedealView.as_view()),
    url(r'^get_packagedeals/?$', PackagedealView.as_view()),
    url(r'^media/(packagedeals/headers/.*)$', django.views.static.serve,{'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),

  ]