# Generated by Django 5.1.1 on 2024-11-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('montant', models.BigIntegerField()),
                ('description', models.TextField(max_length=100)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'budget_budget',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('montant', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
                ('numero_facture', models.CharField(max_length=50, null=True)),
                ('file_facture', models.FileField(blank=True, null=True, upload_to='media/facture')),
                ('description', models.TextField()),
                ('date_depense', models.DateField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'operation_operation',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Perte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('montant', models.BigIntegerField()),
                ('description', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'perte_perte',
                'ordering': ('-id',),
            },
        ),
    ]
