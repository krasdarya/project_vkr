# Generated by Django 4.0.4 on 2022-04-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meteo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meteomodel',
            options={'verbose_name': 'Метеоданные', 'verbose_name_plural': 'Метеоданные'},
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='DP',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Точка росы, C'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='PA',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Атмосферное давление, mm Hg'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='PR',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Количество жидких осадков мгновенное значение, мм'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='PR1H',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Количество жидких осадков сумма за 1 час, мм'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='PR24H',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Количество жидких осадков сумма за сутки, мм'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='RH',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Относительная влажность, %'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='SD_1D',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов относительно            поверхности земли (Вт/м²) суммарное значение за 24 часа'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='SD_1H',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов относительно            поверхности земли (Вт/м²) суммарное значение за 1 час'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='SD_45_1H',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов относительно            поверхности земли (Вт/м²) суммарное значение за 24 часа'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='SR_1M',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Данные от CMP6 установленного параллельно             относительно поверхности земли (Вт/м²) среднее значение за 1 минуту'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='SR_45_1D',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов            относительно поверхности земли (Вт/м²) среднее значение за 24 часа'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='SR_45_1M',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов            относительно поверхности земли (Вт/м²) среднее значение за 1 минуту'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='TA',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Среднее значение температуры за 1 минуту, C'),
        ),
        migrations.AlterField(
            model_name='meteomodel',
            name='WC',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Точка росы, C'),
        ),
    ]
