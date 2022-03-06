from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class NoSignupAdapter(DefaultAccountAdapter):
	"""
	Overrides the default Account Adapter to disable sign-up
	"""
	def is_open_for_signup(self, request):
		return False


class SocialEmailAsUsernameAdapter(DefaultSocialAccountAdapter):
	"""
	Overrides the default Social Account Adapter to always use email address as username
	"""
	def populate_user(self, request, sociallogin, data):
		user = super().populate_user(request, sociallogin, data)
		user.username = user.email
		return user
