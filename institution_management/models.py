from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    objects = BaseManager()
    # not using auto_add and auto_add_now parameters
    # cuz they reported to be buggy
    created_at = models.DateTimeField(
        editable=False, auto_now_add=True, verbose_name=_("Created At")
    )
    updated_at = models.DateTimeField(
        editable=False, auto_now=True, verbose_name=_("Updated At")
    )
    is_deleted = models.BooleanField(null=False, default=False)

    def update(self, to_update):
        """
        updates self with the to_update dict
        """
        for attr, value in to_update.items():
            setattr(self, attr, value)

    class Meta:
        abstract = True
