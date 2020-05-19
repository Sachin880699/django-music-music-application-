# Generated by Django 3.0.5 on 2020-05-17 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Nazwa firmy')),
                ('slug', models.SlugField(unique=True, verbose_name='Adres SEO')),
                ('content', models.TextField(verbose_name='Opis')),
                ('draft', models.BooleanField(default=False, verbose_name='Szablon')),
                ('publish', models.DateField()),
            ],
            options={
                'verbose_name': 'Firma',
                'verbose_name_plural': 'Firmy',
            },
        ),
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Kategoria')),
                ('slug', models.SlugField(unique=True, verbose_name='Adres SEO')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='myapp.Kategoria')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.AddField(
            model_name='firma',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Kategoria', verbose_name='Kategoria'),
        ),
        migrations.AddField(
            model_name='firma',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
    ]
