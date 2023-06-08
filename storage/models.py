# from django.utils.timezone import timezone
# from datetime import *
import datetime as dt
from django.db import models
from django.urls import reverse
from shop.settings import AUTH_USER_MODEL

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    Picture = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})


class Article(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.stock})"


class Box(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for article in self.articles.all():
            article.articled = True
            # article.ordered_date = timezone.localtime()
            article.ordered_date = dt.now()
            article.save()

        self.articles.clear()
        super().delete(*args, **kwargs)
