# Generated by Django 5.0.7 on 2024-09-06 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0005_remove_store_agent_info_store_agent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='store_tel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
