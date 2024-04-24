# Generated by Django 5.0.4 on 2024-04-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('rol', models.CharField(max_length=50)),
                ('yearsExperiencie', models.IntegerField(default=0)),
                ('fechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('state', models.CharField(default='Pendiente', max_length=15)),
                ('fechaInicial', models.DateField()),
                ('fechaEstimada', models.DateField()),
                ('personas', models.ManyToManyField(to='TaskApp.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='tasks',
            field=models.ManyToManyField(to='TaskApp.task'),
        ),
    ]
