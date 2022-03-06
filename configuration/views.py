from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from rest_framework import mixins, viewsets
from speeddater_api import permissions
from configuration.forms import *
from configuration.models import *
from configuration.serializers import *


class MajorViewSet(viewsets.ModelViewSet):
    '''
    View and edit choices of majors.
    - All authenticated users may view (GET) majors.
    - Staff can add (POST), change (PUT/PATCH), and delete (DELETE) majors.
    '''
    queryset = Major.objects.all().order_by('major')
    serializer_class = MajorSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


class SectionTimeViewSet(viewsets.ModelViewSet):
    '''
    View and edit choices of section times.
    - All authenticated users may view (GET) section times.
    - Staff can add (POST), change (PUT/PATCH), and delete (DELETE) section times.
    '''
    queryset = SectionTime.objects.all().order_by('start')
    serializer_class = SectionTimeSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


class SkillViewSet(viewsets.ModelViewSet):
    '''
    View and edit choices of skills.
    - All authenticated users may view (GET) skills.
    - Staff can add (POST), change (PUT/PATCH), and delete (DELETE) skills.
    '''
    queryset = Skill.objects.all().order_by('skill')
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View names and email addresses of users.
    - All authenticated users can only view (GET) user information.
    - To make changes to your own account, see `/rest-auth/user/`.
    '''
    queryset = User.objects.all().order_by('last_name', 'first_name')
    serializer_class = UserSerializer
