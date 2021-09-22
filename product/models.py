from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
import uuid
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Product(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=200)
    desc = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    search_key = models.CharField(max_length=250)
    thumbnail_image = models.ImageField()
    thumbnail_image2 = models.ImageField()
    product_images1 = models.ImageField(blank=True)
    product_images2 = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            name = self.name
            name.replace(" ", "-")
            self.slug = slugify(name + "-" + str(uuid.uuid1()))
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField()


class ProductInquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)
