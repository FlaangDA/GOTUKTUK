
"""
from django.conf.urls import include, url
from django.contrib import admin
from users.views import CreationView, AuthView, AvailabilityView, DriverListView, TripView

print "users/URLS", CreationView
"""

from django.conf.urls import include, url
from django.contrib import admin

# from trip.views import alt som handler om opprettelse av trips.
from views import AvailabilityView, DriverListView, DriverListView
from users import urls as users_urls
from trip import urls as trip_urls
from packagedeals import urls as packagedeals_urls

urlpatterns = [
    url(r'^', include(users_urls)),
    url(r'^', include(trip_urls)),
    url(r'^', include(packagedeals_urls)),

    url(r'^enable_driver?$', AvailabilityView.as_view()),
    url(r'^disable_driver?$', AvailabilityView.as_view()),
    url(r'^available_drivers?$', AvailabilityView.as_view()),

]