# Generated by Django 2.1.15 on 2021-04-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture_info',
            name='tumor_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
