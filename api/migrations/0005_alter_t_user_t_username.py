# Generated by Django 4.1.1 on 2022-09-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_data_email_alter_data_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_user',
            name='t_username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
