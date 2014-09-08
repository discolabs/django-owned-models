from django.db import models
from ..models import UserOwnedModel


class TestUserOwnedModel(UserOwnedModel):
    name = models.CharField(max_length = 16)

    class Meta:
        unique_together = ('user', 'name')
