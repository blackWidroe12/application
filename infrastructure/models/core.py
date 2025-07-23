from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

class Ward(models.Model):
    name = models.CharField(_("Ward Name"), max_length=100)
    code = models.CharField(_("Ward Code"), max_length=20, unique=True)
    population = models.PositiveIntegerField(_("Population"), default=0)
    boundary = models.MultiPolygonField(_("Boundary"), srid=4326)

    class Meta:
        verbose_name = _("Ward")
        verbose_name_plural = _("Wards")

    def __str__(self):
        return f"{self.name} ({self.code})"
