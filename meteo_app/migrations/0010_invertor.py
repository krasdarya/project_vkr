# Generated by Django 4.0.4 on 2022-05-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meteo_app', '0009_delete_author_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invertor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('pv1_input_power', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Входная мощность pv1 (Вт) за 1 сек')),
                ('pv1_voltage', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Напряжение pv1 (В) за 1 сек')),
                ('pv1_current', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Ток pv1 (А) за 1 сек')),
                ('pv2_input_power', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Входная мощность pv2 (Вт) за 1 сек')),
                ('pv2_voltage', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Напряжение pv2 (В) за 1 сек')),
                ('pv2_current', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Ток pv2 (А) за 1 сек')),
                ('grid_voltage', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Напряжение сети (В) за 1 сек')),
                ('grid_current', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Ток сети (А) за 1 сек')),
                ('grid_frequency', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Частота сети (Гц) за 1 сек')),
                ('output_power', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Выходная мощность (Вт) за 1 сек')),
                ('energy_today', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Энергия сегодня (кВт*ч) за 1 сек')),
                ('energy_total', models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Общая энергия (кВт*ч) за 1 сек')),
            ],
            options={
                'verbose_name': 'Данные с инвертора',
                'verbose_name_plural': 'Данные с инвертора',
            },
        ),
    ]
