# Generated by Django 2.2.3 on 2019-08-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_auto_20190826_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link_to_rulebook',
            field=models.URLField(default='www.google.com', max_length=300),
            preserve_default=False,
        ),
    ]
