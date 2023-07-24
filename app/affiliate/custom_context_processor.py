
from django.http import HttpResponse, JsonResponse

from .models import ProductCat,Product_sub_cat, Brand, GenderType, Product

def cats_and_sub_cats(request):
   brands = Brand.objects.all()
   sub_cats = Product_sub_cat.objects.all()
   main_cats = ProductCat.objects.all()
   genders = GenderType.objects.all()
   return ({'sub_cats':sub_cats, 'main_cats':main_cats, 'brand':brands, 'gender':genders})