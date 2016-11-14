from django.core.exceptions import ObjectDoesNotExist


class UserDoesNotExist(ObjectDoesNotExist):

	pass


class AuthViewException(object):

	UserDoesNotExist = UserDoesNotExist

	def doesnotexist(self, user):

		if user:
			return user
		except ObjectDoesNotExist:
			raise UserDoesNotExist