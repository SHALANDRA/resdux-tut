# Generated by Django 3.0.1 on 2021-11-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team_login',
            old_name='Email',
            new_name='access',
        ),
        migrations.RenameField(
            model_name='team_login',
            old_name='Password',
            new_name='password',
        ),
        migrations.AddField(
            model_name='team_login',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team_login',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team_login',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
