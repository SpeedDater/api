from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from django.http import Http404
from django.views.generic import View


class GoogleLoginView(SocialLoginView):
    '''
    Processes Sign-in with Google OAuth.\n
    To sign in with Google, call this endpoint with a Google OAuth `code`
    (recommended), `access_token`, or `id_token`.\n
    Returns an API Token for the authenticated user.
    '''
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.FRONTEND_REDIRECT_URL


class PageNotFoundView(View):
    def get(self, request):
        raise Http404
