from django.conf import settings
from django.db import models


class UserOwnedManager(models.Manager):
    """
    Wraps standard Manager query methods and adds a required `user` argument, to enforce all calls
    made through this manager to be made within a user context.
    """

    def all(self, user):
        return super(UserOwnedManager, self).filter(user = user)

    def filter(self, user, **kwargs):
        return super(UserOwnedManager, self).filter(user = user, **kwargs)

    def exclude(self, user, **kwargs):
        return self.filter(user).exclude(**kwargs)

    def get(self, user, *args, **kwargs):
        return super(UserOwnedManager, self).get(user = user, *args, **kwargs)

    def create(self, user, **kwargs):
        return super(UserOwnedManager, self).create(user = user, **kwargs)

    def get_or_create(self, user, defaults = None, **kwargs):
        if defaults is None:
            defaults = {}
        defaults['user'] = user
        return super(UserOwnedManager, self).get_or_create(user = user, defaults = defaults, **kwargs)

    def update_or_create(self, user, defaults = None, **kwargs):
        if defaults is None:
            defaults = {}
        defaults['user'] = user
        return super(UserOwnedManager, self).update_or_create(user = user, defaults = defaults, **kwargs)


class UserOwnedModel(models.Model):
    """
    Base class for models that are owned by a user.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, editable = False)

    objects = UserOwnedManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
