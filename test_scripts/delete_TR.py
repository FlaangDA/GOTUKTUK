from trip.models import TripRequest


tr = TripRequest.objects.all()[0]

TripRequest.objects.all().delete()

tr.save()