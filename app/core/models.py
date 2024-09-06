"""
Database models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        # password=None because we can create unusable user for some use cases like **test**
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        # If you have multiple databases, its a best practice to do so

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email=email, password=password,
                                extra_fields=extra_fields)
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    # Assign user manager to user model

    USERNAME_FIELD = 'email'
