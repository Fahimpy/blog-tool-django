# Generated by Django 5.1.6 on 2025-02-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_auto_20250211_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='tools',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tools/'),
        ),
    ]
