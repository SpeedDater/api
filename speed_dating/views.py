from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from speeddater_api import permissions
from speed_dating.models import Profile
from speed_dating.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('user')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        # user can only create profile for themselves
        # only staff can create staff for others
        if not request.user.is_staff and request.user.id != request.data.get('user'):
            raise PermissionDenied()
        return super(ProfileViewSet, self).create(request, *args, **kwargs)
