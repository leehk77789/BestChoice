from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_comment',
            name='review_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='review_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='recruit_article',
            name='recruit_join',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.join_article', verbose_name='모집'),
        ),
        migrations.AddField(
            model_name='recruit_article',
            name='recruit_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='join_article',
            name='join_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='join_article',
            name='join_festival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.festival_article', verbose_name='축제'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.join_article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='bookmark_festival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.festival_article'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='bookmark_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
