from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from rest_framework import mixins, viewsets
from speeddater_api import permissions
from configuration.forms import *
from configuration.models import *
from configuration.serializers import *


class MajorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of majors.
    - All authenticated users may view (GET) majors.
    '''
    queryset = Major.objects.all().order_by('major')
    serializer_class = MajorSerializer


class SectionViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of Discussion sections.
    - All authenticated users may view (GET) sections.
    '''
    queryset = Section.objects.all().order_by('number')
    serializer_class = SectionSerializer


class SectionTimeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of section times.
    - All authenticated users may view (GET) section times.
    '''
    queryset = SectionTime.objects.all().order_by('start')
    serializer_class = SectionTimeSerializer


class SkillViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of skills.
    - All authenticated users may view (GET) skills.
    '''
    queryset = Skill.objects.all().order_by('skill')
    serializer_class = SkillSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View names and email addresses of users.
    - All authenticated users can only view (GET) user information.
    - To make changes to your own account, see `/rest-auth/user/`.
    '''
    queryset = User.objects.all().order_by('last_name', 'first_name')
    serializer_class = UserSerializer
