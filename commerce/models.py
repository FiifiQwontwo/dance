from django.db import models
import string
import random


# Create your models here.

def my_slugify(text):
    idn = random.randint(1, 50000)
    text = text.lower()
    unsafe = [letter for letter in text if letter == " "]
    if unsafe:
        for letter in unsafe:
            text = text.replace(letter, '-')
    text = u'_'.join(text.split())
    text = f'{text}-{idn}'
    return text


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=250, blank=True)
    product_category_image = models.ImageField(upload_to='category', blank=True)
    slug = models.SlugField()
    # user = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)


class Ids(models.Model):
    id_type = models.CharField(max_length=100)
    id_example = models.ImageField(upload_to='id_examples', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.id_type

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.id_type)
        super(Ids, self).save(*args, **kwargs)


class VendorSign(models.Model):
    name_of_vendor = models.CharField(max_length=50)
    name_of_shop = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15)
    phone_number1 = models.CharField(max_length=15, blank=True)
    biz_registration = models.ImageField(upload_to='Vendor_biz_registration', blank=True)
    shop_place_image = models.ImageField(upload_to='Vendor_shops', blank=True)
    id_type = models.ForeignKey(Ids, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=50, unique=True)
    id_image = models.ImageField(upload_to='ids_of_vendor')
    current_image = models.ImageField(upload_to='vendors_image', blank=True, help_text='current image please')
    email_add = models.EmailField(unique=True, max_length=250)
    location = models.CharField(max_length=250, blank=True)
    category = models.ManyToManyField(ProductCategory)
    slug = models.SlugField(unique=True)
    # user = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_vendor + ' - ' + self.name_of_shop

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.name_of_vendor + ' - ' + self.name_of_shop)
        super(VendorSign, self).save(*args, **kwargs)


class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_short_name = models.CharField(max_length=100, blank=True, help_text='A short name eg.Iphone SE')
    product_brand = models.CharField(max_length=250, help_text='a brand name eg. Apple')
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=15, decimal_places=2)
    product_discount_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    # discount_percentage = models.
    product_image = models.ImageField(upload_to='products')
    product_image_1 = models.ImageField(upload_to='products', blank=True)
    product_image_2 = models.ImageField(upload_to='products', blank=True)
    product_image_3 = models.ImageField(upload_to='products', blank=True)
    product_image_4 = models.ImageField(upload_to='products', blank=True)
    product_image_5 = models.ImageField(upload_to='products', blank=True)
    product_video = models.FileField(upload_to='videos/', blank=True)
    product_stock = models.IntegerField()
    operating_system = models.CharField(max_length=25, blank=True)
    #product_size = models.CharField()
    available = models.BooleanField(default=True)
    vendor = models.ForeignKey(VendorSign, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    # user = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_short_name

    def save(self, *args, **kwargs):
        self.slug = my_slugify(self.product_short_name)
        super(Product, self).save(*args, **kwargs)


# how to add a copyright water to images django

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['created_at']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def subtotal(self):
        return self.quantity * self.product.product_price

    def __str__(self):
        return self.product


class ProductAfter(models.Model):
    product_name = models.CharField(max_length=250)
    product_short_name = models.CharField(max_length=100, blank=True, help_text='A short name eg.Iphone SE')
    product_brand = models.CharField(max_length=250, help_text='a brand name eg. Apple')
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=15, decimal_places=2)
    product_discount_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    # discount_percentage = models.
    product_image = models.ImageField(upload_to='products')
    product_image_1 = models.ImageField(upload_to='products', blank=True)
    product_image_2 = models.ImageField(upload_to='products', blank=True)
    product_image_3 = models.ImageField(upload_to='products', blank=True)
    product_image_4 = models.ImageField(upload_to='products', blank=True)
    product_image_5 = models.ImageField(upload_to='products', blank=True)
    product_video = models.FileField(upload_to='videos/', blank=True)
    product_stock = models.IntegerField()
    operating_system = models.CharField(max_length=25, blank=True)
    #product_size = models.CharField()
    available = models.BooleanField(default=True)
    vendor = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    # user = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
