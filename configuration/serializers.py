from django.contrib.auth.models import User
from rest_framework import serializers
from configuration.models import *


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['url', 'major']


class SectionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTime
        fields = ['url', 'start', 'end']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['url', 'skill']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'email']
