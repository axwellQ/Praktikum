from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)
    is_published = models.BooleanField(default=True)


class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    is_published = models.BooleanField(default=True)


class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)


class IceCream(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    # Связь "Один ко многим" (N:1): Обязательное поле, каскадное удаление
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    # Связь "Многие ко многим" (N:M): Обязательное поле (по умолчанию)
    toppings = models.ManyToManyField(Topping)

    # Связь "Один к одному" (1:1): Необязательное поле, при удалении ставится NULL
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )