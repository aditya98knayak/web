# Generated by Django 2.2.3 on 2019-12-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=90)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
