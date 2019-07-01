# Generated by Django 2.2.3 on 2019-07-01 18:24

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('companyname', models.CharField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('reason', models.TextField()),
                ('resume', models.FileField(null=True, upload_to=student.models.upload_status_image)),
                ('datetimestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='StudentLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=256)),
                ('course', models.CharField(max_length=256)),
                ('semester', models.IntegerField()),
                ('department', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('mobno', models.BigIntegerField()),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TPO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]