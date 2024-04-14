# Generated by Django 3.2 on 2024-04-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_is_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=320, null=True)),
                ('phone_number', models.CharField(max_length=320)),
                ('profession', models.CharField(blank=True, max_length=320, null=True)),
            ],
        ),
    ]