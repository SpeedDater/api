from rest_framework import serializers
from configuration.serializers import *
from speed_dating.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'phone', 'current_section', 'availability', 'majors',
                  'interests', 'skills', 'looking_for', 'anything_else']
