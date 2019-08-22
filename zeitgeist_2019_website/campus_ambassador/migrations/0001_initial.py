# Generated by Django 2.2.3 on 2019-08-20 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('campus_ambassador_code', models.CharField(max_length=15, unique=True, verbose_name='CA Code')),
                ('college', models.CharField(max_length=200, verbose_name='College Name')),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN', verbose_name='Mobile Number')),
                ('why_interested', models.TextField(verbose_name='Why do you want to be a Campus Ambassador?')),
                ('past_experience', models.TextField(verbose_name='Do you have any past experience related to this? If yes, then please share your experience')),
            ],
            options={
                'verbose_name_plural': 'Registration details',
            },
        ),
    ]
