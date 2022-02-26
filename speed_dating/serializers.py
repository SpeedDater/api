from rest_framework import serializers
from configuration.serializers import *
from speed_dating.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    availability = SectionTimeSerializer(many=True)
    majors = MajorSerializer(many=True)
    interests = SkillSerializer(many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = Profile
        fields = ['user', 'phone', 'availability', 'majors',
                  'interests', 'skills', 'looking_for', 'anything_else']
