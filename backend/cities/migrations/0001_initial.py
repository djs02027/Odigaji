# Generated by Django 4.0.3 on 2022-03-29 02:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recommends', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('population', models.IntegerField()),
                ('area', models.FloatField()),
                ('photo', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='profile_images/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city')),
                ('taste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommends.taste')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.province'),
        ),
        migrations.AddField(
            model_name='city',
            name='rate_users',
            field=models.ManyToManyField(default='', related_name='rate_cities', through='cities.Visit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('facilities', models.TextField(max_length=100)),
                ('parking_lot', models.IntegerField()),
                ('tel', models.CharField(max_length=15)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.province')),
            ],
        ),
    ]
