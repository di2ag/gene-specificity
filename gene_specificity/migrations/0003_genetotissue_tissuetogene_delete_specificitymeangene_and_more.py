# Generated by Django 4.1 on 2023-12-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gene_specificity', '0002_curietemplate_curietemplatematch'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneToTissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(db_index=True, max_length=255)),
                ('tissue_id', models.CharField(max_length=255)),
                ('spec', models.FloatField()),
                ('norm_spec', models.FloatField()),
                ('p_val', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TissueToGene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(max_length=255)),
                ('tissue_id', models.CharField(db_index=True, max_length=255)),
                ('spec', models.FloatField()),
                ('norm_spec', models.FloatField()),
                ('p_val', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='SpecificityMeanGene',
        ),
        migrations.DeleteModel(
            name='SpecificityMeanTissue',
        ),
        migrations.DeleteModel(
            name='SpecificityMedianGene',
        ),
        migrations.DeleteModel(
            name='SpecificityMedianTissue',
        ),
    ]
