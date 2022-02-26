from django.contrib.auth.models import User
from rest_framework import serializers
from configuration.models import *


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['id', 'major']


class SectionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTime
        fields = ['id', 'start', 'end']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
