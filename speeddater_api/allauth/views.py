from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.http import Http404
from django.views.generic import View


class GoogleLoginView(SocialLoginView):
    '''
    A view for handling Google OAuth2 login
    '''
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'http://127.0.0.1:8000/oauth/step2/'


class PageNotFoundView(View):
    def get(self, request):
        raise Http404
