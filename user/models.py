from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, User


class profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userImage = models.ImageField('Profile Image', upload_to='profileImages/', null=True)
    birthday = models.DateField('Date of birthday', default='1999-01-01')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

        # userImage = models.ImageField('Profile Image', upload_to='profileImages/', null=True)
        # birthday = models.DateField('Date of birthday', default='01.01.1999')