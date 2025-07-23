from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .core import Ward

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'System Administrator'),
        ('planner', 'Planning Officer'),
        ('field', 'Field Officer'),
        ('public', 'Public User'),
    ]
    role = models.CharField(_("System Role"), max_length=20, choices=ROLE_CHOICES, default='public')
    wards = models.ManyToManyField(Ward, verbose_name=_("Assigned Wards"), blank=True)
    phone = models.CharField(_("Phone Number"), max_length=20, blank=True)
    profile_image = models.ImageField(_("Profile Image"), upload_to='profiles/', null=True, blank=True)
    last_location = models.PointField(_("Last Known Location"), geography=True, srid=4326, null=True, blank=True)
    location_timestamp = models.DateTimeField(_("Location Timestamp"), null=True, blank=True)
    # Fix reverse accessor clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='infrastructure_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='infrastructure_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    @property
    def is_field_officer(self):
        return self.role == 'field'
    @property
    def can_edit(self):
        return self.role in ['admin', 'planner', 'field']