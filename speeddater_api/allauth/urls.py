from importlib import import_module
from django.urls import include, path
from allauth import app_settings
from allauth.account import views as account_views
from allauth.socialaccount import views as social_views
from allauth.socialaccount import providers
from speeddater_api.allauth.views import PageNotFoundView

# taken from allauth/account/urls.py, without signup and password-related stuff
urlpatterns = [
    path('signup/', PageNotFoundView.as_view(), name='account_signup'),
    path('login/', account_views.login, name='account_login'),
    path('logout/', account_views.logout, name='account_logout'),
    path('inactive/', account_views.account_inactive, name='account_inactive'),
]

# taken from allauth/socialaccount/urls.py, without signup
if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [
        path('login/cancelled/', social_views.login_cancelled,
             name='socialaccount_login_cancelled'),
        path('login/error/', social_views.login_error,
             name='socialaccount_login_error'),
    ]

# directly taken from allauth/urls.py
# Provider urlpatterns, as separate attribute (for reusability).
provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + '.urls')
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns
