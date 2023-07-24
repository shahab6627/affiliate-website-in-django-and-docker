from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index,name="index" ),
    
    # path('data', views.all_products,name="allpro" ), 
    
    path('blog/<str:slug>', views.blogs_details, name="blog-details"),
    path('brand/<str:slug>', views.brandProducts, name='brand_details'),
    path('<str:slug>/details', views.product_details, name="product_details"),
    path('category/<str:slug>', views.product_cats, name="product_cats"),
    path('comment/comment-post', views.postComment, name="comment"),
]