from rest_framework.viewsets import mixins, GenericViewSet
from .models import Registration, Work
from .serializers import RegistrationSerializer, WorkSerializers, WorkCraeteSerializers
from rest_framework.permissions import IsAdminUser, AllowAny


class RegistrationViewSet(mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            GenericViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partail_update']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class WorkViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):

    queryset = Work.objects.all()
    serializer_class = WorkSerializers


    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partail_update']:
            self.permission_classes = [IsAdminUser]
        if self.action in ['list', 'retrive']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            return WorkCraeteSerializers
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context



