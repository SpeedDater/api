from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from speeddater_api import permissions
from configuration.forms import *
from configuration.models import *
from configuration.serializers import *


class MajorViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows majors to be viewed or edited.
	"""
	queryset = Major.objects.all().order_by('major')
	serializer_class = MajorSerializer
	permission_classes = [permissions.IsAdminOrReadOnly]


class SectionTimeViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows section times to be viewed or edited.
	"""
	queryset = SectionTime.objects.all().order_by('start')
	serializer_class = SectionTimeSerializer
	permission_classes = [permissions.IsAdminOrReadOnly]


class SkillViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows section times to be viewed or edited.
	"""
	queryset = Skill.objects.all().order_by('skill')
	serializer_class = SkillSerializer
	permission_classes = [permissions.IsAdminOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows Users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('last_name', 'first_name')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticatedAndReadOnly]
