'''openapi URL Configuration

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
from django.conf import settings
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view
from openapi import views
from openapi.schema_generator import SpeedDaterSchemaGenerator

app_name = 'openapi'
api_title = f'{settings.APP_NAME} API' 

urlpatterns = [
    path('openapi', get_schema_view(title=api_title,
                                    version=settings.APP_VERSION,
                                    generator_class=SpeedDaterSchemaGenerator,
                                    permission_classes=[AllowAny],
                                    public=True), name='schema'),
    path('docs/', views.SwaggerUIView.as_view(), name='swagger'),
]
