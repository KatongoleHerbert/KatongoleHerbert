from accounts.models import User
from django.db.models import Q


class TauthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False


    def get_user(self, user_id):
       try:
          return User.objects.get(pk=user_id)
       except User.DoesNotExist:
          return None

    def authenticate(self, std_id, password):
        try:
            user = User.objects.get(
                Q(std_id=std_id)
            )
        except User.DoesNotExist:
            return None

        return user if user.check_password(password) else None