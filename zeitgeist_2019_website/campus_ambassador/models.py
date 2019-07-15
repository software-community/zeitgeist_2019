from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class RegistrationDetails(models.Model):
    college = models.CharField(max_length=200, verbose_name='College Name')
    # would have liked to use PhoneNumberField from phonenumber_field.modelfields
    # pip install django-phonenumber-field
    # pip install phonenumbers (or) pip install phonenumberslite
    mobile_number = PhoneNumberField(null=False, blank=False, verbose_name='Mobile Number', region='IN')
    why_interested = models.TextField(verbose_name='Why do you want to be a Campus Ambassador?')
    past_experience = models.TextField(verbose_name='Do you have any past experience related to this? If yes, then please share your experience')
    campus_ambassador_code = models.CharField(max_length=15, verbose_name='CA code')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name_plural = 'Registration details'

    def __str__(self):
        return 'Registration by ' + str(self.user)
