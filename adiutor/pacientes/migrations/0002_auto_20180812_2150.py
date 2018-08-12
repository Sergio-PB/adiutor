# Generated by Django 2.1 on 2018-08-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='Celular',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Fixo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Parentesco',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Responsavel',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Sexo',
            field=models.CharField(choices=[('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Termino',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Whats',
            field=models.IntegerField(null=True),
        ),
    ]
