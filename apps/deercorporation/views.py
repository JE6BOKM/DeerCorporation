from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from apps.deercorporation.models import RideHistory
from apps.deercorporation.serializers import RideHistroySerializer


class RideHistroyView(CreateModelMixin, ListModelMixin, GenericAPIView):

    queryset = RideHistory.objects.all()
    serializer_class = RideHistroySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        if self.request.method == "GET":
            queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
