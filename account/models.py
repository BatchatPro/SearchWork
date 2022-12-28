from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager

JOB_TYPE = (
    ('E', "Erkak"),
    ('A', "Ayol"),

)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, error_messages={
                                  'unique': "Ushbu emaildan foydalana olmaysiz.(avval ro'yhatdan o'tgan)",
                             })
    role = models.CharField(choices=ROLE, max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)
    phont_number = models.CharField(max_length=25)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()
