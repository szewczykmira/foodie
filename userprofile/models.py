from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='E-mail')
    fb_id = models.CharField(verbose_name='Id', max_length=30, primary_key=True)
    first_name = models.CharField(verbose_name='First name', max_length=15)
    last_name = models.CharField(verbose_name='Last name', max_length=15)
    is_active = models.BooleanField(verbose_name='Is active', default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
