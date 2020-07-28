from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField("Category", max_length=50)
    description = models.TextField('Description')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Genre(models.Model):
    name = models.CharField("Genre", max_length=50)
    description = models.TextField('Description')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Game(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, verbose_name='Genres')
    price = models.FloatField(default=0)
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    rating = models.IntegerField()
    release = models.IntegerField()
    poster = models.ImageField('Poster', null=True, upload_to='gamesImage/')
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField('Editor', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'


class GameShots(models.Model):
    title = models.CharField("Category", max_length=50)
    description = models.TextField('Description')
    image = models.ImageField('Image', null=True, upload_to='GameShots/')
    game = models.ForeignKey(Game, verbose_name='Game', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Game shot'
        verbose_name_plural = 'Game shots'


class Reviews(models.Model):
    name = models.CharField("Category", max_length=50)
    text = models.TextField('Description')
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    game = models.ForeignKey(Game, verbose_name='Game', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.game}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
