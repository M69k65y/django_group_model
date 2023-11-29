from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Inject fields into `Group` model.
if not hasattr(Group, "created_at"):
    created_at_field = models.DateTimeField(
        _("Created At"),
        blank=True,
        null=True,
        editable=False,
        default=timezone.now,
    )
    created_at_field.contribute_to_class(Group, "created_at")
