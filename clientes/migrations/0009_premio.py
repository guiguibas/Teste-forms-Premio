# Generated by Django 2.1.2 on 2018-11-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_funcionarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('chave_premio', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('dt_inclus', models.DateTimeField()),
                ('ctr_custo', models.CharField(max_length=12)),
                ('tipo', models.PositiveIntegerField()),
                ('competenc', models.CharField(max_length=7)),
                ('observacao', models.CharField(blank=True, max_length=1000, null=True)),
                ('cpf', models.PositiveIntegerField()),
                ('nota_camp', models.CharField(blank=True, max_length=20, null=True)),
                ('vlr_base', models.DecimalField(decimal_places=2, max_digits=7)),
                ('falta_just', models.CharField(blank=True, max_length=3, null=True)),
                ('falta_inju', models.CharField(blank=True, max_length=3, null=True)),
                ('vlr_pagar', models.DecimalField(decimal_places=2, max_digits=7)),
                ('solicitante', models.TextField()),
                ('dt_env_cpa', models.DateTimeField()),
                ('dt_pagamento', models.DateTimeField()),
                ('sit_empre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': '[DBO].[GESTAO_PREMIACAO]',
            },
        ),
    ]
