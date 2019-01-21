# Generated by Django 2.1.5 on 2019-01-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate', to='article.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='high_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hcate', to='article.Category'),
        ),
    ]
