from django.contrib.auth.models import AbstractUser
from django.db import models  # Add this import

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='infrastructure_user_set',
        related_query_name='infrastructure_user',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='infrastructure_user_set',
        related_query_name='infrastructure_user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )

    class Meta:
        db_table = 'infrastructure_user'