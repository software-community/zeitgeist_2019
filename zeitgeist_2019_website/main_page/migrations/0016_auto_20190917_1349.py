# Generated by Django 2.2.3 on 2019-09-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0015_event_link_to_rulebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='aadhar_no',
            field=models.CharField(max_length=5, verbose_name='Last 4 digits of your Aadhar Number'),
        ),
    ]
