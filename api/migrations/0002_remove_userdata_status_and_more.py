# Generated by Django 5.0.1 on 2024-02-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='status',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='transaction',
        ),
        migrations.AddField(
            model_name='userdata',
            name='status_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdata',
            name='status_unpaid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdata',
            name='transactions',
            field=models.ManyToManyField(to='api.transaction'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
