from django.conf import settings
from users.models import CustomUser
from django.contrib.auth.hashers import check_password


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
