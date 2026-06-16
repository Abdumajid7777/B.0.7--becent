from django.shortcuts import render, redirect


from main.models import Product, Category
# Create your views here.



def main(reguest):
    product_list = Product.objects.all()
    categorys_list = Category.objects.all()
    return render(reguest, 'index.html', {
        "product_list":  product_list,
        "categorys_list": categorys_list,
    }) 


def about(request):
    return render(request, "about.html")


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product_detail.html", {
        "product": product
    })





def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        color = request.POST.get('color')
        description = request.POST.get('description')
        category = request.POST.get('category')

        Product.objects.create(
            name=name,
            price=price,
            color=color,
            description=description,
            category=category,
        )
        return redirect('main')

    groups = Category.objects.all()
    return render(request, 'create_product.html', {'groups': groups})


def update_product(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.color = request.POST.get('color')
        product.description = request.POST.get('description')
        product.category = request.POST.get('category')

        if request.FILES.get('avatar'):
            product.avatar = request.FILES.get('avatar')

        product.save()
        return redirect('main')

    return render(request, 'update_product.html', {'product': product, 'category': category})





 
def category_detail(request, id):
    category = Category.objects.get(id=id)
    return render(request, "category_detail.html", {
        "category": category
    })


def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_count = request.POST.get('category_count')

        Category.objects.create(
            name=name,
            category_count=category_count,
        )
        return redirect('main')



def update_category(request, id):
    category = Category.objects.get(id=id)

    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.category_count = request.POST.get('category_count')

        category.save()
        return redirect('main')

    return render(request, 'update_product.html', {'category': category})

