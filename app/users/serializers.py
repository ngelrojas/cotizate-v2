from django.core.validators import EmailValidator
from rest_framework import serializers, fields
from rest_framework.generics import get_object_or_404
from core.user import User
from core.encoder_tokens import encode_user_id
from core.encoder_tokens import make_user_token
from api.celery import send_email_module
from api.settings import production

URL_SEND_EMAIL = production.URL_PRODUCTION
ACTIVATION_ACCOUNT = "/activar-cuenta"
RECOVERY_PASSWORD = "/recuperar-contrasena"


class UserSerializer(serializers.ModelSerializer):
    """model user serializer"""

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "password", "deleted")
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5},
            "deleted": {"write_only": True},
        }
        read_only_fields = ("id",)

    def create(self, validate_data):
        """create user"""
        user_instance = User.objects.create_user(**validate_data)
        uid = encode_user_id(user_instance.id)
        token = make_user_token(user_instance)
        url = f"{URL_SEND_EMAIL}"
        context_page = ACTIVATION_ACCOUNT
        email_context = {
            "fullname": f'{validate_data["first_name"]}',
            "domain": url + context_page,
            "uid": uid,
            "token": token,
        }
        tmp_name = "emails/confirm_activated_email.html"
        send_email_module.delay(
            subject="No reply",
            to=[validate_data["email"]],
            body="",
            template_name=tmp_name,
            context=email_context,
        )

        return user_instance

    def update(self, instance, validate_data):
        """update password current user"""
        password = validate_data.pop("password", None)
        user = super().update(instance, validate_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class RecoveryPwdSerializer(serializers.ModelSerializer):
    """model recovery password serializer"""

    email = fields.EmailField(validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ("email",)

    def create(self, validate_data):
        """send email to recovery password"""
        user = get_object_or_404(User, email=validate_data.get("email"))
        uid = encode_user_id(user.id)
        token = make_user_token(user)
        url = f"{URL_SEND_EMAIL}"
        context_page = RECOVERY_PASSWORD
        email_context = {
            "fullname": f'{validate_data["user.first_name"]}',
            "domain": url + context_page,
            "uid": uid,
            "token": token,
        }
        tmp_name = "emails/recovery_password_email.html"
        send_email_module.delay(
            subject="Cotizate - Recovery Password",
            to=[validate_data["email"]],
            body="",
            template_name=tmp_name,
            context=email_context,
        )
        return validate_data


class PwdConfirmSerialzier(serializers.ModelSerializer):
    """confirm password serializer"""

    password = fields.CharField(style={"input_type": "password"}, required=True,)
    password_confirm = fields.CharField(
        style={"input_type": "password"}, required=True,
    )

    class Meta:
        model = User
        fields = ("password", "password_confirm")

    def validate(self, attrs):
        """validation data password and password confirm"""
        if attrs.get("password") != attrs.get("password_confirm"):
            raise serializers.ValidationError("Those passwords don't match")
        return attrs
