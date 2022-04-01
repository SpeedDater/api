from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from rest_framework import mixins, viewsets, views
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from speeddater_api import permissions
from speeddater_api.helpers import PageNumberPagination25
from teams.models import Team
from teams.serializers import *


class TeamViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    View and edit the team that the student is a part of.
    - All authenticated users can view (GET), edit (POST/PUT/PATCH), and 
      delete (DELETE) the team they are a part of.
    - If user attempts to add a person to an empty team (or when student isn't
      in a team yet), a new team will be created automatically.
    '''
    queryset = Team.objects.all().order_by('number')
    lookup_field = 'number'
    pagination_class = PageNumberPagination25
    permission_classes = [permissions.IsAdminOwnerOrReadOnly]
    serializer_class = TeamSerializer


class TeamMemberView(views.APIView):
    '''
    View and edit team members in a specified team.
    - All authenticated users can view (GET), edit (POST/PUT/PATCH), and 
      delete (DELETE) team members of the team they are a part of.

    Response format:
    ```json
    {
        "members": [
            user_id (integer),
            ...
        ]
    }
    ```
    '''

    def get_team_number(number_str):
        try:
            return int(number_str)
        except ValueError:
            return None

    def get(self, request, format=None, *args, **kwargs):
        number = kwargs['number']
        try:
            team = Team.objects.get(number=number)
        except (Team.DoesNotExist, ValueError):
            return Response({'error': f'{number} is not a valid team number.'}, status=400)
        # return team members
        members = get_team_members(team)
        return Response({'members': members}, status=200)

    def put(self, request, format=None, *args, **kwargs):
        number = kwargs['number']
        try:
            team = Team.objects.get(number=number)
        except Team.DoesNotExist:
            return Response({'error': f'{number} is not a valid team number.'}, status=400)
        # can't edit teams that user isn't a part of
        if not request.user.is_staff and request.user.id not in members:
            raise PermissionDenied()
        # parse request body
        try:
            member_ids = request.data['members']
        except KeyError:
            return Response({'error': f'Invalid request body: missing "members" list.'}, status=400)

        # clear current member list
        clear_team_members(team)
        # build new member list
        for m_id in member_ids:
            try:
                m = User.objects.get(id=m_id)
                add_team_member(team, User.objects.get(id=m_id))
            except User.DoesNotExist:
                return Response({'error': f'User ID {m_id} is invalid.'}, status=400)

        # save changes
        try:
            team.save()
        except (IntegrityError, ValidationError) as e:
            return Response({'error': str(e)}, status=400)
        # respond with new member list
        members = get_team_members(team)
        return Response({'members': members}, status=201)
