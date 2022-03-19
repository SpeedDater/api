from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from speeddater_api import permissions
from teams.models import Team
from teams.serializers import TeamSerializer


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
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        '''
        Standard create() method, but user can only create teams for
        themselves, and only staff can create teams for others.
        '''
        if not request.user.is_staff and request.user.id not in request.data.get('members'):
            raise PermissionDenied()
        return super(TeamViewSet, self).create(request, *args, **kwargs)
