from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage, Category
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request, category_slug=None):

    category = None
    productlist = Product.objects.all()
    categorylist = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        productlist = productlist.filter(category=category)

    context = {'product_list': productlist, 'category_list':categorylist, 'category':category }

    template = 'home.html'

    return render(request, template, context)

def productlist(request, category_slug=None):

    category = None


    productlist = Product.objects.all()

    if category_slug:
        category = Category.objects.get(slug = category_slug)
        productlist = productlist.filter(category=category)

    context = {'product_list': productlist }
    template = 'product/product_list.html'

    return render(request, template, context)

def productgrid(request, category_slug=None):

    category = None


    productlist = Product.objects.all()

    if category_slug:
        category = Category.objects.get(slug = category_slug)
        productlist = productlist.filter(category=category)

    context = {'product_list': productlist }
    template = 'product/product_grid.html'

    return render(request, template, context)

def productdetail(request, id):
    productdetail = Product.objects.get(id = id)
    productimages = ProductImage.objects.filter(product=productdetail)
    context = {'product_detail': productdetail, 'product_images':productimages }
    template = 'product/product_detail.html'

    return render(request, template, context)

def uploadanimal(request):
    if request.method == 'POST'and request.FILES['myfile']:
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        city = request.POST.get('city')
        mobilenumber = request.POST.get('mobilenumber')

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        image = fs.url(filename)
        b = Product(name = name, description=description, price=price, city=city,  image = image, mobilenumber=mobilenumber)
        b.save()
    context = {}
    template = 'product/upload.html'
    return render(request, template, context)
