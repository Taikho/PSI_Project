# Generated by Django 3.1.5 on 2021-01-26 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210126_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='DodatkoweInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rodzaj', models.IntegerField(choices=[(3, 'Spodniczka'), (1, 'Sukienka'), (5, 'Spodnie'), (0, 'Nieznany'), (2, 'Suknia'), (4, 'Zakiet')], default=0)),
                ('material', models.TextField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='dodatkowe_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.dodatkoweinfo'),
        ),
    ]
