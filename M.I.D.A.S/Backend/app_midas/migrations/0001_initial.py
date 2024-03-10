# Generated by Django 5.0.2 on 2024-03-10 20:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ClientGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_groups', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_groups', to='app_midas.group')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategies', to='app_midas.commodity')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='strategies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StrategySite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strategy_sites', to='app_midas.site')),
                ('strategy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strategy_sites', to='app_midas.strategy')),
            ],
        ),
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tokens', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StrategyToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strategy_tokens', to='app_midas.strategy')),
                ('token', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strategy_tokens', to='app_midas.tokens')),
            ],
        ),
    ]
