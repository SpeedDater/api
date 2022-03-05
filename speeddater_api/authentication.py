from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.authentication import TokenAuthentication


class GoogleLoginView(SocialLoginView):
	"""
	A view for handling Google OAuth2 login
	"""
	adapter_class = GoogleOAuth2Adapter
	client_class = OAuth2Client
	callback_url = 'http://127.0.0.1:8000/oauth/step2/'


class SocialAccountEmailAsUsername(DefaultSocialAccountAdapter):
	"""
	Overrides the default Social Account Adapter to always use email address as username
	"""
	def populate_user(self, request, sociallogin, data):
		user = super().populate_user(request, sociallogin, data)
		user.username = user.email
		return user


class BearerAuthentication(TokenAuthentication):
	"""
	A token-based authenticator that uses the standard "Authorization: Bearer" header
	"""
	keyword = "Bearer"
