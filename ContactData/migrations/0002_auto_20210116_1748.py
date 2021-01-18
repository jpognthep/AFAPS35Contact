# Generated by Django 3.0.5 on 2021-01-16 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ContactData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuserdata',
            name='Domicile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='provinceBirth', to='ContactData.TProvince'),
        ),
        migrations.AlterField(
            model_name='tuserdata',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='provinceWork', to='ContactData.TProvince'),
        ),
    ]