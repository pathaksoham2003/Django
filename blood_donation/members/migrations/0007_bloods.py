# Generated by Django 4.2.1 on 2023-10-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_remove_users_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byid', models.IntegerField(null=True)),
                ('byname', models.CharField(max_length=25, null=True)),
                ('litresofblood', models.IntegerField(null=True)),
                ('bloodGroup', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]