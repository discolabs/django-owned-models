from django.conf import settings
from django.db import models


class UserOwnedModelManager(models.Manager):

    def filter_for_user(self, user, *args, **kwargs):
        return super(UserOwnedModelManager, self).get_queryset().filter(user = user, *args, **kwargs)

    def get_for_user(self, user, *args, **kwargs):
        if 'user' in kwargs:
            kwargs.pop('user')
        return super(UserOwnedModelManager, self).get_queryset().get(user = user, *args, **kwargs)

    def get_or_create_for_user(self, user, **kwargs):
        return super(UserOwnedModelManager, self).get_or_create(user = user, **kwargs)

class UserOwnedModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable = False)

    objects = UserOwnedModelManager()

    class Meta:
        abstract = True