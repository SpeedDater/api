"""frontend_test URL Configuration

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
from django.urls import path, include
from frontend_test import views

app_name = 'frontend_test'

urlpatterns = [
    path('', views.OAuthStep1.as_view(), name="step1"),
    path('step2/', views.OAuthStep2.as_view(), name="step2"),
    path('logout/', views.OAuthLogout.as_view(), name="logout"),
]
