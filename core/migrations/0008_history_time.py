# Generated by Django 3.0.4 on 2020-04-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]