# Generated by Django 3.1.7 on 2021-04-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_name',
            new_name='product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
