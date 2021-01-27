# Generated by Django 3.1.5 on 2021-01-26 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210126_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(2, 'Suknia'), (3, 'Spodniczka'), (5, 'Spodnie'), (4, 'Zakiet'), (1, 'Sukienka'), (0, 'Nieznany')], default=0),
        ),
        migrations.CreateModel(
            name='Opinia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst_rec', models.TextField(default='')),
                ('gwiazdy', models.IntegerField(default=0)),
                ('produkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
        ),
    ]
