from django.shortcuts import render


from main.models import Product
# Create your views here.



def main(reguest):
    product_list = Product.objects.all()
    return render(reguest, 'index.html', {
        "product_list":  product_list
    }) 
