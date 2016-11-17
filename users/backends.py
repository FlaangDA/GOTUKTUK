from django.conf import settings
from users.models import CustomUser
from django.contrib.auth.hashers import check_password
from users.models import CustomUser
from django.contrib.auth.backends import ModelBackend
import facebook

class EmailAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """

    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        try:
            user = CustomUser.objects.get(email=email)
            if check_password(password, user.password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
"""
class FacebookBackend(ModelBackend):

    def authenticate(self, fb_uid=None, fb_graphtoken=None, email):

    If we receive a facebook uid then the cookie has already been
    validated.

    if fb_uid:
        user, created = CustomUser.objects.get(email=email)
        return user
    return None


class FacebookProfileBackend(ModelBackend):
    Authenticate a facebook user and autopopulate facebook data into the
    user's profile.
    def authenticate(self, fb_uid=None, fb_graphtoken=None):

        If we receive a facebook uid then the cookie has already been
        validated.

        if fb_uid and fb_graphtoken:

            user, created = CustomUser.objects.get_or_create(facebook.GraphAPI(fb_graphtoken).get_object('me'))
            if created:
                # It would be nice to replace this with an asynchronous request
                graph = facebook.GraphAPI(fb_graphtoken)
                me = graph.get_object('me')
                if me:
                    if me.get('first_name'):
                        user.first_name = me['first_name']
                    if me.get('last_name'):
                        user.last_name = me['last_name']
                    if me.get('email'):
                        user.email = me['email']
                    if me.get('email'):
                        user.dob 
                    user.save()
            return user
        return None
"""