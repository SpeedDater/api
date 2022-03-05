"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from speeddater_api.social_account import GoogleLoginView
import configuration.views
import speed_dating.views

router = routers.DefaultRouter()
router.register('majors', configuration.views.MajorViewSet)
router.register('profiles', speed_dating.views.ProfileViewSet)
router.register('sections', configuration.views.SectionTimeViewSet)
router.register('skills', configuration.views.SkillViewSet)
router.register('users', configuration.views.UserViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    # Django authentication
    path('accounts/', include('allauth.urls')),
    # dj-rest-auth
    path('accounts/rest-auth/', include('dj_rest_auth.urls')),
    path('accounts/rest-auth/google/', GoogleLoginView.as_view()),
    # Extra admin pages
    path('admin/', include('admin_pages.urls', namespace="admin_pages")),
    # Django admin
    path('admin/', admin.site.urls),
    # OpenAPI and Swagger UI
    path('', include('openapi.urls', namespace="openapi")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
