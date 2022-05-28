from email.policy import default
from django.db import models

class StatusMixin(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
