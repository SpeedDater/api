from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from configuration import forms, models, serializers


class MajorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of majors.
    - All authenticated users may view (GET) majors.
    '''
    queryset = models.Major.objects.all().order_by('major')
    serializer_class = serializers.MajorSerializer


class SectionViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of Discussion sections.
    - All authenticated users may view (GET) sections.
    '''
    queryset = models.Section.objects.all().order_by('number')
    serializer_class = serializers.SectionSerializer


class SectionTimeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of section times.
    - All authenticated users may view (GET) section times.
    '''
    queryset = models.SectionTime.objects.all().order_by('start')
    serializer_class = serializers.SectionTimeSerializer


class SkillViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View the list of skills.
    - All authenticated users may view (GET) skills.
    '''
    queryset = models.Skill.objects.all().order_by('skill')
    serializer_class = serializers.SkillSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View names and email addresses of users.
    - All authenticated users can only view (GET) user information.
    - To make changes to your own account, see `/rest-auth/user/`.
    '''
    queryset = User.objects.all().order_by('last_name', 'first_name')
    serializer_class = serializers.UserSerializer
