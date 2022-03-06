from django.conf import settings
from django.urls import path
from dj_rest_auth import views

# taken from dj_rest_auth/urls.py, without password-related stuff
urlpatterns = [
    # URLs that do not require a session or valid token
    path('login/', views.LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    path('logout/', views.LogoutView.as_view(), name='rest_logout'),
    path('user/', views.UserDetailsView.as_view(), name='rest_user_details'),
]

# taken from dj_rest_auth/urls.py
if getattr(settings, 'REST_USE_JWT', False):
    from rest_framework_simplejwt.views import TokenVerifyView
    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', views.TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', views.get_refresh_view().as_view(), name='token_refresh'),
    ]
