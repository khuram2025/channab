from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    mobilenumber = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='main_img/', blank=True, null=True, default='main_img/1.jpg')
    created = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    def __str__(self):
        return self.product.name


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    description = models.TextField()

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('product_list_category', args=[self.slug])
