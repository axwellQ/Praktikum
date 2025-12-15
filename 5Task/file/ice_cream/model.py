from django.db import models

# Импортируем абстрактную модель из приложения core
from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)
    # Поле is_published удалено, так как оно наследуется от PublishedModel


class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    # Поле is_published удалено


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256)
    # Поле is_published удалено


class IceCream(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)
    # Поле is_published удалено

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    toppings = models.ManyToManyField(Topping)
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )