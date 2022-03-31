from django.conf import settings
from django.views.generic import TemplateView


class OAuthStep1(TemplateView):
	template_name = 'oauth_step1.html'

	def get_context_data(self, **kwargs):
		context = {
			'client_id': settings.SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id'],
			'redirect_uri': settings.FRONTEND_REDIRECT_URL,
			'scope': 'profile email',
		}
		return context


class OAuthStep2(TemplateView):
	template_name = 'oauth_step2.html'


class OAuthLogout(TemplateView):
	template_name = 'oauth_logout.html'
