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
from django.views.generic.base import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
import configuration.views
import speed_dating.views

router = routers.DefaultRouter()
router.register('majors', configuration.views.MajorViewSet)
router.register('profiles', speed_dating.views.ProfileViewSet)
router.register('sections', configuration.views.SectionTimeViewSet)
router.register('skills', configuration.views.SkillViewSet)
router.register('users', configuration.views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/configuration/bulk_update/', configuration.views.BulkUpdateView.as_view(), name="bulk_update"),
    path('admin/configuration/bulk_update/major/', configuration.views.MajorBulkUpdateView.as_view(), 
         name="bulk_update_major"),
    path('admin/configuration/bulk_update/skill/', configuration.views.SkillBulkUpdateView.as_view(),
         name="bulk_update_skill"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('openapi', get_schema_view(title="SpeedDater407", version="1.0.0"), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
            template_name='swagger.html', extra_context={'schema_url':'openapi-schema'}
        ), name='swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
