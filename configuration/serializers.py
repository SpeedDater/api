from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from rest_framework import serializers
from configuration.models import *


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['id', 'major']


class SectionSerializer(serializers.ModelSerializer):
    start_time = serializers.CharField(source='time.start', read_only=True)
    end_time = serializers.CharField(source='time.end', read_only=True)
                 
    class Meta:
        model = Section
        fields = ['id', 'number', 'start_time', 'end_time']


class SectionTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTime
        fields = ['id', 'start', 'end']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'skill']


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField(read_only=True)

    def get_profile_picture(self, obj):
        try:
            # look up profile picture from social account
            social_account = SocialAccount.objects.get(user=obj)
            profile_pic = social_account.extra_data['picture']
            return profile_pic
        except SocialAccount.DoesNotExist:
            # not social account. no profile pic
            return None

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'profile_picture']
