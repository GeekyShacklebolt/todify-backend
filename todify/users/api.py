# Third Party Stuff
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from . import models, serializers, services


class AuthUserViewset(viewsets.GenericViewSet):

    permission_classes = [AllowAny, ]
    queryset = models.User.objects.all()
    serializer_class = serializers.RegisterUserSerializer

    @action(methods=["POST"], detail=False)
    def register(self, request):
        serializer = serializers.RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = services.create_user_account(**serializer.validated_data)
        data = serializers.UserProfileSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)


class CurrentUserViewset(viewsets.GenericViewSet,
                         generics.DestroyAPIView,
                         generics.UpdateAPIView):

    permission_classes = [IsAuthenticated, ]
    serializer_class = serializers.UserProfileSerializer
    queryset = models.User.objects.all()

    def get_serializer_class(self):
        if self.action in ('avatar_upload', 'avatar_remove'):
            return serializers.CurrentUserAvatarSerializer
        elif self.action in ('password_change',):
            return serializers.PasswordChangeSerializer
        return serializers.UserProfileSerializer

    def get_object(self):
        return self.request.user

    def list(self, request):
        """Get logged in user profile"""
        serializer = self.get_serializer(self.get_object())
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=False)
    def password_change(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["POST"], detail=False)
    @parser_classes((FormParser, MultiPartParser))
    def avatar_upload(self, request, pk=None):
        instance = self.get_object()
        if request.FILES:
            data = request.data
            serializer = self.get_serializer(instance, data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            serializer = serializers.UserProfileSerializer(instance)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["DELETE"], detail=False)
    @parser_classes((FormParser, MultiPartParser))
    def avatar_remove(self, request, pk=None):
        instance = self.get_object()
        if not instance.avatar:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instance.avatar.delete(save=True)
        serializer = self.get_serializer(instance)
        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)


class UserViewset(viewsets.GenericViewSet,
                  generics.RetrieveAPIView,
                  generics.ListAPIView):

    permission_classes = [AllowAny, ]
    serializer_class = serializers.UserProfileSerializer

    def get_queryset(self):
        queryset = models.User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
