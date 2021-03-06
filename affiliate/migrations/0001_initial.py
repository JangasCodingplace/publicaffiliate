# Generated by Django 3.1.2 on 2020-10-06 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'unique_together': {('family', 'version')},
            },
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'unique_together': {('family', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, help_text='If blank it gets autogenerated. **Max 16 Chars.**', max_length=16, unique=True)),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=144)),
                ('request_count', models.IntegerField(default=0, editable=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links_created_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('family', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'unique_together': {('brand', 'family', 'model')},
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('ua_string', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('ip', models.GenericIPAddressField(editable=False)),
                ('browser', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='affiliate.browser')),
                ('device', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='affiliate.device')),
                ('link', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='client_where_link_is_in', to='affiliate.link')),
                ('os', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='affiliate.os')),
            ],
        ),
    ]
