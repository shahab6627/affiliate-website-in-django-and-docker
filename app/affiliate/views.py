from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import ProductCat,Product_sub_cat,Product, Blog, Brand, Comment
import json
# Create your views here.

def index(request):
    product_cats = ProductCat.objects.all()
    products = Product.objects.select_related('product_brand').exclude(status ='pending')    
    # print(products)
    blogs = Blog.objects.all()
    for b in blogs:
        print(b)
    return render(request, 'affiliate/index.html', {'product_cats':product_cats, 'products':products, 'blogs':blogs})


def blogs_details(request,slug):
    blog = Blog.objects.get(slug = slug)
    blog_cat = blog.blog_cat
    blog_by_cat = Blog.objects.filter(blog_cat = blog_cat).exclude(slug = slug)
    blog_comments = Comment.objects.filter(blog_id = blog.id)
    
    return render(request, 'affiliate/blog_details.html', {'blog':blog, 'blog_cat':blog_by_cat, 'blog_comments':blog_comments})

def brandProducts(request, slug):
    brand = Brand.objects.get(slug = slug)
    brand_name = brand.brand_name
    brand_products = Product.objects.filter(product_brand = brand.id)
    other_products = Product.objects.exclude(product_brand = brand.id)
    return render(request, 'affiliate/brand_products.html', {'products':brand_products,'other_products':other_products,'brand_name':brand_name})

    



def product_details(request, slug):
    prodDetails = Product.objects.filter(slug = slug).first()
    
    similer_brand_products = Product.objects.filter(product_brand = prodDetails.product_brand).exclude(id = prodDetails.id)
    related_products = Product.objects.filter(product_main_cat_id = prodDetails.product_main_cat_id)
    
    return render(request, 'affiliate/product_details.html', {'product':prodDetails, 'similer_brand_products':similer_brand_products, 'related_products':related_products})


def product_cats(request, slug):
    sub_cat = Product_sub_cat.objects.get(slug = slug)
    sub_cat_id = sub_cat.id
    cat_products = Product.objects.filter(product_sub_cate = sub_cat_id)
    blogs = Blog.objects.filter(blog_cat = sub_cat.main_cat_id)
    other_products = Product.objects.exclude(product_sub_cate = sub_cat_id)
    return render(request, 'affiliate/category.html', {'products':cat_products, 'cat_name':sub_cat.sub_cat_name, 'other_products':other_products, 'blogs':blogs})



def postComment(request):
    if request.is_ajax:
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        blog_id = request.POST.get('blog_id')

        saveComment = Comment.objects.create(name = name, email=email, comment=comment, blog_id = blog_id)
        saveComment.save()
        return JsonResponse({'message':'comment is posted... after approvel your comment will be shown'})


    return JsonResponse({'message':'ok'})