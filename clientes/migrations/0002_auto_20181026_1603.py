# Generated by Django 2.1.2 on 2018-10-26 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
            options={
                'db_table': '[MLSF\\guilherme.neto].[GESTAO_PREMIACAO]',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='clientes_fotos'),
        ),
    ]