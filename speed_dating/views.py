from rest_framework import viewsets
from api import permissions
from speed_dating.models import Profile
from speed_dating.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('user')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminOwnerOrReadOnly]
