from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import AllowAny

from apps.deercorporation.models import RideHistory
from apps.deercorporation.serializers import RideHistroySerializer


class RideHistroyView(RetrieveModelMixin, GenericAPIView):

    queryset = RideHistory.objects.all()
    serializer_class = RideHistroySerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
