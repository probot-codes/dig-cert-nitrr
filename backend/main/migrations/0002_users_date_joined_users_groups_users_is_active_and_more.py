# Generated by Django 4.2.5 on 2023-10-18 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='users',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]