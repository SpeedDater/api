'''api URL Configuration

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
'''
from allauth.account import views as allauth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from speeddater_api.allauth.views import GoogleLoginView
import configuration.views
import speed_dating.views
import teams.views

router = routers.DefaultRouter()
router.register('majors', configuration.views.MajorViewSet)
router.register('profiles', speed_dating.views.ProfileViewSet)
router.register('sections', configuration.views.SectionViewSet)
router.register('section-times', configuration.views.SectionTimeViewSet)
router.register('skills', configuration.views.SkillViewSet)
router.register('teams', teams.views.TeamViewSet)
router.register('users', configuration.views.UserViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    # django-allauth (using a subset of its urls)
    path('auth/', include('speeddater_api.allauth.urls')),
    # dj-rest-auth
    path('rest-auth/', include('speeddater_api.allauth.restauth_urls')),
    path('rest-auth/google/login/', GoogleLoginView.as_view(),
         name='rest_login_google'),
    # Extra admin pages
    path('admin/', include('admin_pages.urls', namespace='admin_pages')),
    # Django admin
    path('admin/', admin.site.urls),
    # OpenAPI and Swagger UI
    path('', include('openapi.urls', namespace='openapi')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
