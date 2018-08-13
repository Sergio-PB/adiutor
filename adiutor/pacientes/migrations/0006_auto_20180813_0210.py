# Generated by Django 2.1 on 2018-08-13 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20180812_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='prontuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prontuario', models.IntegerField()),
                ('texto', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='Status',
            field=models.CharField(choices=[('ANAMNESE', 'Deve ser feita anamnese'), ('ATENDIMENTO', 'Está sendo atendido'), ('LICENCA', 'Em licença'), ('ENCERRADO', 'Encerrado')], default='ANAMNESE', max_length=15),
        ),
        migrations.AddField(
            model_name='prontuarios',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.pacientes'),
        ),
    ]
