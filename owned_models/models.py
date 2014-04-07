from django.conf import settings
from django.db import models


class UserOwnedModelManager(models.Manager):

    def filter_for_user(self, user):
        return super(UserOwnedModelManager, self).get_queryset().filter(user = user)


class UserOwnedModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable = False)

    objects = UserOwnedModelManager()

    class Meta:
        abstract = True