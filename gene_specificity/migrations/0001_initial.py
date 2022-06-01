# Generated by Django 4.0.4 on 2022-05-31 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificityMeanGene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_curie', models.CharField(max_length=255)),
                ('tissue_curie', models.CharField(max_length=255)),
                ('specificity_mean', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecificityMeanTissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tissue_curie', models.CharField(max_length=255)),
                ('gene_curie', models.CharField(max_length=255)),
                ('specificity_mean', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecificityMedianGene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_curie', models.CharField(max_length=255)),
                ('tissue_curie', models.CharField(max_length=255)),
                ('specificity_median', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecificityMedianTissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tissue_curie', models.CharField(max_length=255)),
                ('gene_curie', models.CharField(max_length=255)),
                ('specificity_median', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('query', models.JSONField(default=dict)),
                ('status', models.CharField(default='', max_length=100, null=True)),
                ('versions', models.JSONField(default=dict)),
                ('chp_app', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
