from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class user(models.Model):
    username = models.CharField(_("Username"), max_length=255,unique=True)
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self) -> str:
        return f'{self.username}'

class email(models.Model):
    username = models.ForeignKey(user,to_field="username",related_name="email", on_delete=models.CASCADE)
    email = models.EmailField(_("Email ID"), max_length=254)

    def __str__(self) -> str:
        return f'{self.username}'