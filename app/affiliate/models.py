from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from smart_selects.db_fields import ChainedForeignKey
from django.urls import reverse
from smart_selects.db_fields import ChainedManyToManyField
# from djangotoolbox.fields import ListField
# Create your models here.

class GenderType(models.Model):
    gender = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.gender

class ProductCat(models.Model):
    
    cat_name = models.CharField(max_length=100,blank=True, null=True)
    cat_image = models.ImageField(upload_to='images/cat_images', blank=True, null=True)
    cat_icon = models.FileField(upload_to='images/icons', blank=True, null=True, help_text="(select svg file)")
    url_text = models.CharField(max_length=200, blank=True, null=True)
    
    slug = AutoSlugField(null=True, unique=True, populate_from='url_text', max_length=100,always_update=True)
    def __str__(self):
        return self.cat_name
    
    def get_products(self):
        return self.product_set.all()

class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.color_name

class Product_sub_cat(models.Model):
    sub_cat_name = models.CharField(max_length=100)
    main_cat = models.ForeignKey(ProductCat, on_delete=models.CASCADE, related_name="main_cat")
    url_text = models.CharField(max_length=200, blank=True, null=True)
    gender_type = models.ForeignKey(GenderType, on_delete=models.CASCADE, null=True, blank=True)
    slug = AutoSlugField(null=True, unique=True, populate_from='sub_cat_name', max_length=100,always_update=True)
    
    def __str__(self):
        return self.sub_cat_name
    
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    barnd_logo = models.FileField(upload_to='images/brand_logo')
    parama_link = models.CharField(max_length=200)
    
    slug = AutoSlugField(null=True, unique=True, populate_from='parama_link', max_length=100,always_update=True)
    
    def __str__(self):
        return self.brand_name
    
    def get_absolute_url(self):
        return reverse('brand_details', args = {self.slug} )

    

class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_main_cat = models.ForeignKey(ProductCat, on_delete=models.CASCADE, related_name="product_main_cat1", blank=True, null=True)
    product_sub_cate = ChainedManyToManyField(
        Product_sub_cat,
        chained_field="product_main_cat",
        chained_model_field="main_cat",
       
    )

    color_name = models.ManyToManyField(Color)
    material_type = models.CharField(max_length=200, blank=True, null=True)
    item_weight = models.CharField(max_length=200, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="producut_brand")
    
    product_home_page_image = models.ImageField(upload_to='images/product_images', help_text="(This Picture Will be displyed on home page")
    product_detail_image = models.ImageField(upload_to="images/detail_images", help_text="(This Picture will be displayed on product detail page")
    product_detail_image1 = models.ImageField(upload_to="images/detail_images", help_text="(This Picture will be displayed on product detail page1", blank=True, null=True)
    product_detail_image2 = models.ImageField(upload_to="images/detail_images", help_text="(This Picture will be displayed on product detail page2", blank=True, null=True)
    
    PRODUCT_SIZE_LIST = (
		('inches', 'inches'),
		('feet', 'feet'),
		('meter', 'meter'),  
    )
    product_long_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parama_link = models.CharField(max_length=255)
    affiliate_link = models.URLField(
        max_length=128, 
        null=True,
        blank=True
    )
    gender_type = models.ForeignKey(GenderType, on_delete=models.CASCADE, null=True, blank=True)
    slug = AutoSlugField(null=True, unique=True, populate_from='parama_link',always_update=True)
    PRODUCT_STATUS = (
        ('pending','pending'),
        ('posted','posted')
        )
    status = models.CharField(max_length = 100, choices=PRODUCT_STATUS)
    def __str__(self):
        return self.product_title
    
    def get_absolute_url(self):
        return reverse('product_details', args = {self.slug} )


class Blog(models.Model):
    
    blog_title = models.CharField(max_length=200)
    blog_pic = models.ImageField(upload_to="images/blog-pics")
    blog_short_description = models.TextField()
    blog_body = models.TextField()
    blog_cat = models.ForeignKey(ProductCat, on_delete=models.CASCADE)
    parma_link = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, populate_from='parma_link', always_update=True)
    
    create_at = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.blog_title
    
    def get_absolute_url(self):
    	return reverse('blog-details', args = {self.slug} )



class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name