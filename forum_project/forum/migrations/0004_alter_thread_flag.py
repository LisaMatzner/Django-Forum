# Generated by Django 5.1.5 on 2025-02-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_thread_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='flag',
            field=models.CharField(choices=[('default', 'Normal'), ('closed', 'Closed'), ('pinned', 'Pinned'), ('new', 'New')], default='new', max_length=20),
        ),
    ]
