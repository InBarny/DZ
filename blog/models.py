from django.db import models

# Create your models here.
# https://azinkin.ru/orm.html

class Category(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Post(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=255,
    )
    content = models.TextField(
        verbose_name='контент',
        blank=True,
    )
    picture = models.ImageField(
        verbose_name='картинка',
        blank=True,
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=False,
    )
    category = models.ForeignKey(
        verbose_name='категория',
        to='Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'публикации'
        unique_together = ('category', 'slug')


class Coment(models.Model):
    post = models.ForeignKey(
        verbose_name="Публикация",
        to='Post',
        on_delete=models.CASCADE
)
    name = models.CharField(
        verbose_name="Имя",
        max_length=255
    )

    content = models.TextField(
        verbose_name="Комментарий"
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания"
    )

    parent_comment = models.ForeignKey(
        verbose_name="Родительский комментарий",
        to='self',
        on_delete=models.CASCADE,
        null = True
    )

    def __str__(self):
        return f"Комментарий от {self.name} к {self.post.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class lick (models.Model):
    post = models.ForeignKey(
        verbose_name="Публикация",
        to='Post',
        on_delete=models.CASCADE
)
    created_at = models.DateTimeField(
        verbose_name="Дата создания"
)
    estimation = (
        (1, 'лайк'),
        (2, 'нелайк')
    )

    reaction = models.IntegerField(
        verbose_name="Реакция",
        choices=estimation
    )

    def __str__(self):
        return f"Реакция на {self.post.title}"

    class Meta:
        verbose_name = "Реакция"
        verbose_name_plural = "Реакции"
        


class Donat(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=255
)
    link = models.URLField(
        verbose_name="Ссылка"
)
    image = models.ImageField(
        verbose_name="Картинка"
)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Донат"
        verbose_name_plural = "Донаты"