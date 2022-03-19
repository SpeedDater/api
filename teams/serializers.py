from rest_framework import serializers
from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    def get_members(self, obj):
        get_team_members(obj)

    class Meta:
        model = Team
        fields = ['number', 'members', 'availability', 'preferred_section',
                  'assigned_section']


def get_team_members(team):
    # create members list with every non-null member
    members = []
    if team.member1:
        members.append(team.member1.id)
    if team.member2:
        members.append(team.member2.id)
    if team.member3:
        members.append(team.member3.id)
    if team.member4:
        members.append(team.member4.id)
    if team.member5:
        members.append(team.member5.id)
    return members


def add_team_member(team, new_member):
    # add member to team
    if not team.member1:
        team.member1 = new_member
    elif not team.member2:
        team.member2 = new_member
    elif not team.member3:
        team.member3 = new_member
    elif not team.member4:
        team.member4 = new_member
    elif not team.member5:
        team.member5 = new_member


def clear_team_members(team):
    # remove all team members
    team.member1 = None
    team.member2 = None
    team.member3 = None
    team.member4 = None
    team.member5 = None
