from django.db import models

class StrMixin(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        abstract = True
