from rest_framework import serializers
from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['members', 'availability', 'preferred_section',
                  'assigned_section']
