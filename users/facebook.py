from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache

from social_auth.models import UserSocialAuth
from social_auth.views import complete as social_complete
from social_auth.backends.facebook import FacebookBackend