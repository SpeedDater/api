from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from speeddater_api import permissions
from teams.models import Team
from teams.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    '''
    View and edit student teams.
    - All authenticated users can view (GET) teams. Authenticated users can
      also create (POST), edit (PUT/PATCH), and delete (DELETE) the team they
      are a part of.
    - Staff can also create (POST), edit (PUT/PATCH), and delete (DELETE)
      all teams.
    '''
    queryset = Team.objects.all().order_by('id')
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
