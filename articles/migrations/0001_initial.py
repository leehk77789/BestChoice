from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Festival_Article',
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("festival_title", models.CharField(default="", max_length=50)),
                ("festival_desc", models.TextField()),
                ("festival_address", models.CharField(max_length=50)),
                ("festival_region", models.CharField(max_length=50)),
                ("festival_date", models.CharField(max_length=50)),
                ("festival_image", models.CharField(max_length=100)),
                ("festival_price", models.CharField(max_length=30)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('festival_title', models.CharField(default='', max_length=50)),
                ('festival_desc', models.TextField()),
                ('festival_address', models.CharField(max_length=50)),
                ('festival_region', models.CharField(max_length=50)),
                ('festival_date', models.CharField(max_length=50)),
                ('festival_image', models.CharField(max_length=100)),
                ('festival_price', models.CharField(max_length=30)),
                ('festival_cost', models.CharField(max_length=10)),
                ('festival_start', models.DateField()),
                ('festival_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Join_Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_title', models.CharField(max_length=20)),
                ('join_count', models.IntegerField(default=0)),
                ('join_desc', models.TextField()),
                ('join_period', models.DateField()),
                ('join_status', models.BooleanField(default=False)),
                ('join_created_at', models.DateTimeField(auto_now_add=True)),
                ('join_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruit_Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit_introduce', models.TextField()),
                ('recruit_status', models.BooleanField(default=False)),
                ('recruit_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=20)),
                ('review_desc', models.TextField()),
                ('review_created_at', models.DateTimeField(auto_now_add=True)),
                ('review_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_comment', models.TextField()),
                ('review_comment_created_at', models.DateTimeField(auto_now_add=True)),
                ('review_comment_updated_at', models.DateTimeField(auto_now=True)),
                ('review_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.review')),
            ],
        ),
    ]
