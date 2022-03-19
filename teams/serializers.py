from rest_framework import serializers
from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    def get_members(self, obj):
        # create members list with every non-null member
        members = []
        if obj.member1:
            members.append(obj.member1.id)
        if obj.member2:
            members.append(obj.member2.id)
        if obj.member3:
            members.append(obj.member3.id)
        if obj.member4:
            members.append(obj.member4.id)
        if obj.member5:
            members.append(obj.member5.id)
        return members

    class Meta:
        model = Team
        fields = ['number', 'members', 'availability', 'preferred_section',
                  'assigned_section']
