from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='изображение'),
        ),
    ]
