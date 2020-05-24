from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from core.user import User
from core.encoder_tokens import decode_user_id
from users.serializers import UserSerializer
from users.serializers import RecoveryPwdSerializer
from users.serializers import PwdConfirmSerialzier
from api.cotizate import ActiveUser


class CreateUserView(generics.CreateAPIView):
    """Create new user"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UpdateUserView(viewsets.ModelViewSet):
    """update main data current user"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, pk=None):
        """retrieve current user"""
        try:
            current_user = ActiveUser.currentUser(self, request)
            serializer = self.serializer_class(current_user)
            return Response({'data': serializer.data},
                            status=status.HTTP_200_OK)
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        """update data partial current user"""
        current_user = ActiveUser.currentUser(self, request)
        serializer = self.serializer_class(
            current_user,
            data=request.data,
            partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data': 'user updated'},
                            status=status.HTTP_200_OK)
        return Response({'error': 'something wrong happend'},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """update state current user to deleted"""
        try:
            current_user = self.currentUser(request)
            current_user.deleted = True
            current_user.is_activate = False
            current_user.save()
            return Response({'data': 'user deleted'},
                            status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)


class RecoveryPasswordUser(viewsets.ModelViewSet):
    """recovery send email current user password"""
    serializer_class = RecoveryPwdSerializer
    queryset = User.objects.all()


class RecoveryPwdConfirm(viewsets.ModelViewSet):
    """recovery password confirmations"""
    serializer_class = PwdConfirmSerialzier
    queryset = ''

    def update(self, request, **kwargs):
        """method to recovery password user"""
        try:
            uid = decode_user_id(request.data.get('uid'))
            token = request.data.get('token')
            current_user = get_object_or_404(User, id=uid)
            if current_user.is_activate and token:
                serializer = self.serializer_class(
                    data=request.data,
                    partial=True
                )
                if serializer.is_valid(raise_exception=True):
                    current_user.set_password(request.data.get('password'))
                    current_user.save()
                    return Response({'data': 'password updated.'},
                                    status=status.HTTP_200_OK)

                return Response({'error': 'user is not activated.'},
                                status=status.HTTP_200_OK)
            return Response({'error': 'some of data is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as err:
            return Response({'error': f'{err}'},
                            status=status.HTTP_404_NOT_FOUND)
