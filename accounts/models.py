from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('farmer', 'Farmer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')

    # make email unique to avoid duplicate accounts with same email
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return f"{self.username} ({self.role})"
