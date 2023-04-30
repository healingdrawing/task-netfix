from django.contrib.auth.backends import BaseBackend
from base.models import Kastrat


class EmailBackend(BaseBackend):
    def authenticate(self, request=None, email=None, password=None, **kwargs):
        try:
            user = Kastrat.objects.get(email=email)
        except Kastrat.DoesNotExist:
            return None

        if password is not None and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Kastrat.objects.get(pk=user_id)
        except Kastrat.DoesNotExist:
            return None
