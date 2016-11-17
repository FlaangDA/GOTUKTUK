from django.conf.urls import include, url
from django.contrib import admin

from views import TripView
import django
from src import settings
urlpatterns = [
	
    url(r'^finish_trip?$', TripView.as_view()),
    url(r'^request_trip?$', TripView.as_view()),
    url(r'^ping_triprequest?$', TripView.as_view()),
    url(r'^accept_triprequest?$', TripView.as_view()),
    url(r'^check_triprequest?$', TripView.as_view()),
    url(r'^check_price$', TripView.as_view()),
    url(r'^get_trip_graphics$', TripView.as_view()),
    url(r'^cancel_trip$', TripView.as_view()),
 	url(r'^media/(tripsession/.*)$', django.views.static.serve,{'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),


]