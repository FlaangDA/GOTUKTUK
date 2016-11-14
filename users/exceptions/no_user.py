from django.core.exceptions import ObjectDoesNotExist


class UserDoesNotExist(ObjectDoesNotExist):

	pass


class AuthViewException(object):

	UserDoesNotExist = UserDoesNotExist

	def exception_no_user(self, user):

		try user:
			return user
		except ObjectDoesNotExist:
			raise ObjectDoesNotExist