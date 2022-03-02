"""admin_pages URL Configuration

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
from admin_pages import views

app_name = 'admin_pages'

urlpatterns = [
    path('auth/user/add-staff/', views.AddStaffView.as_view(), name="add_staff"),
    path('configuration/major/bulk-import/', views.MajorBulkUpdateView.as_view(),
         name="bulk_import_major"),
    path('configuration/skill/bulk-import/', views.SkillBulkUpdateView.as_view(),
         name="bulk_import_skill"),
]