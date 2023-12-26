from django.db import models
from django_mysql.models.functions import JSONField
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(models.Model):
    fa_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['fa_name']

    def __str__(self):
        return self.fa_name


class Brand(models.Model):
    fa_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='brand_logo/')

    def __str__(self):
        return self.fa_name


class AttributeCategory(models.Model):
    fa_name = models.CharField(max_length=100)

    def __str__(self):
        return self.fa_name


class ProductAttribute(models.Model):
    fa_name = models.CharField(max_length=100)

    def __str__(self):
        return self.fa_name


class Product(models.Model):
    fa_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.CharField(max_length=500)
    full_description = models.TextField()
    toman_price = models.PositiveIntegerField(default=0)
    inventory = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    product_attribute = models.ManyToManyField(ProductAttribute, through='ProductAttributeValue')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.fa_name


class ProductColor(models.Model):
    fa_name = models.CharField(max_length=255)

    def __str__(self):
        return self.fa_name


class ProductDynamicProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = JSONField()


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(ProductColor, on_delete=models.PROTECT)
    sku = models.CharField(max_length=80, unique=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product} : {self.color} : {self.quantity}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return self.product.fa_name + ' Image'


class ProductComment(models.Model):
    COMMENT_STATUS_WAITING = 'w'
    COMMENT_STATUS_APPROVED = 'a'
    COMMENT_STATUS_CANCEL = 'na'
    COMMENT_STATUS_CHOICES = [(COMMENT_STATUS_WAITING, 'waiting'), (COMMENT_STATUS_APPROVED, 'approved'),
                              (COMMENT_STATUS_CANCEL, 'Not approved')]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    recommend = models.BooleanField(default=True)
    comment_status = models.CharField(max_length=2, choices=COMMENT_STATUS_CHOICES, default=COMMENT_STATUS_APPROVED)
