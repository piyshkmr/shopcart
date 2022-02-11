# Generated by Django 3.2.5 on 2021-08-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210805_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Electronics', 'Electronics'), ('Education', 'Education'), ('Essentials', 'Essentials')], max_length=50),
        ),
    ]
