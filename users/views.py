from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import IsSelfUser
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsAuthenticated,)
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.action in ["retrieve", "update", "partial_update"]:
            self.permission_classes = [IsAuthenticated, IsSelfUser]

        return super().get_permissions()
