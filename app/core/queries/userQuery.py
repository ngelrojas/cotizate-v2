from core.user import User


class UserQuery:
    """all about user query"""

    @staticmethod
    def is_user(request):
        return User.objects.get(id=request.user.id)
