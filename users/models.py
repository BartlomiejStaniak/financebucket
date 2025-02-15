from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    role_choices = [
        ("admin", "Admin"),
        ("client", "Client"),
        ("investor", "Investor"),

    ]

    role = models.CharField(max_length=20, choices=role_choices, default="client")
    email = models.EmailField(max_length=60)
    username = models.CharField(max_length=60, unique=True)



    def __str__(self):
        return self.username
