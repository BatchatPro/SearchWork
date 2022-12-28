from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password, **extra_fields):
        """
        User email va password bilan yaratiladi va saqlanadi.
        """
        if not email:
            raise ValueError('Email kiritishingiz shart.')
        if not password:
            raise ValueError('Password kiritishingiz shart.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        SupperUser email va password bilan yaratiladi va saqlanadi.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuserda is_staff=True bo\'lishi shart.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuserda is_superuser=True bo\'lishi shart.')
        return self.create_user(email, password, **extra_fields)