from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from .core import Ward

class InfrastructureType(models.Model):
    name = models.CharField(_("Type Name"), max_length=50, unique=True)
    icon = models.CharField(_("Icon Code"), max_length=30, blank=True)
    color = models.CharField(_("Map Color"), max_length=7, default='#3388ff')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Infrastructure(models.Model):
    ASSET_STATUS = [
        ('active', 'Active'),
        ('planned', 'Planned'),
        ('damaged', 'Damaged'),
        ('decommissioned', 'Decommissioned'),
    ]
    name = models.CharField(_("Asset Name"), max_length=255)
    type = models.ForeignKey(InfrastructureType, on_delete=models.PROTECT)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT)
    status = models.CharField(_("Status"), max_length=20, choices=ASSET_STATUS, default='active')
    geom = models.GeometryField(_("Location"), srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_inspected = models.DateField(_("Last Inspection"), null=True, blank=True)
    metadata = models.JSONField(_("Additional Data"), default=dict, blank=True)
    class Meta:
        ordering = ['-updated_at']
    def __str__(self):
        return f"{self.type.name}: {self.name} ({self.ward.name})"

class Road(Infrastructure):
    ROAD_CLASS = [
        ('highway', 'Highway'),
        ('primary', 'Primary Road'),
        ('secondary', 'Secondary Road'),
        ('tertiary', 'Tertiary Road'),
        ('track', 'Track'),
    ]
    length_km = models.FloatField(_("Length (km)"))
    surface_type = models.CharField(_("Surface Type"), max_length=50)
    road_class = models.CharField(_("Road Class"), max_length=20, choices=ROAD_CLASS)
    lanes = models.PositiveSmallIntegerField(_("Number of Lanes"), default=2)
    class Meta:
        verbose_name = _("Road")
        verbose_name_plural = _("Roads")

class Building(Infrastructure):
    BUILDING_TYPES = [
        ('clinic', 'Clinic'),
        ('school', 'School'),
        ('office', 'Government Office'),
        ('residential', 'Residential'),
    ]
    building_type = models.CharField(_("Building Type"), max_length=20, choices=BUILDING_TYPES)
    floor_count = models.PositiveSmallIntegerField(_("Floors"), default=1)
    capacity = models.PositiveIntegerField(_("Capacity"), null=True, blank=True)
    class Meta:
        verbose_name = _("Building")
        verbose_name_plural = _("Buildings")