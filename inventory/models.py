from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('distributor', 'Distributor'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES)
    status = models.CharField(max_length=20, default='Pending')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"