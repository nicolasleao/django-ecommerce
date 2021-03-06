# Generated by Django 2.2.7 on 2019-11-23 23:29

import app_store.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=60, unique=True)),
                ('domain', models.CharField(default='', max_length=150, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('visible', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_store.Store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('visible', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_store.Store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('storecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_store.StoreContent')),
                ('description', models.TextField(default='', max_length=1200)),
                ('model', models.CharField(default='', max_length=100)),
                ('price_new', models.FloatField(default=0)),
                ('price_old', models.FloatField(default=0)),
                ('image', models.ImageField(upload_to=app_store.utils.product_thumbnail_path)),
                ('total_sales', models.PositiveIntegerField(blank=True, default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='app_store.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('app_store.storecontent',),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('storecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_store.StoreContent')),
                ('code', models.CharField(default='', max_length=60)),
                ('percentage', models.FloatField(default=0)),
                ('expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ManyToManyField(to='app_store.Category')),
                ('products', models.ManyToManyField(to='app_store.Product')),
            ],
            options={
                'abstract': False,
            },
            bases=('app_store.storecontent',),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('storecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_store.StoreContent')),
                ('products', models.ManyToManyField(to='app_store.Product')),
            ],
            options={
                'abstract': False,
            },
            bases=('app_store.storecontent',),
        ),
    ]
