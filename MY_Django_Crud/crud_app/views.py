from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from crud_app import forms
#Models import
from crud_app.models import Brand, Product

def index(request, deleteText='no'):
    form = forms.BrandForm()
    brandList = Brand.objects.all()
    if request.method == "POST":
        form = forms.BrandForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.BrandForm()

    diction = {
        'title': 'Home | CRUD',
        'formBrand':form,
        'brandList':brandList,
        'deleteText':deleteText
    }
    return render(request, 'crud_app/index.html', context=diction)

def ProductView(request, deleteText='no'):
    productForm = forms.ProductForm()
    productList = Product.objects.all()
    if request.method  == "POST":
        productForm = forms.ProductForm(request.POST)

        if productForm.is_valid():
            productForm.save(commit=True)
            productForm = forms.ProductForm()


    diction = {
        'title': 'Product | CRUD',
        'productForm':productForm,
        'productList':productList,
        'deleteText':deleteText
    }
    return render(request, 'crud_app/product_form_list.html', context=diction)


def BrandProduct(request, proudctBrand_id):
    productList = Product.objects.filter(proudctBrand_id=proudctBrand_id)
    brand = Brand.objects.filter(pk=proudctBrand_id)

    #title with brand
    for row in brand :
         name = row.brandName
         #title with brand
    diction = {
        'title': name+' | CRUD',
        'productList':productList,
        'brand':brand
    }
    return render(request, 'crud_app/brand_product_list.html', context=diction)

def editBrand(request, id):
    updateText = 'no'
    brand = Brand.objects.get(pk=id)
    Editform = forms.BrandForm(instance=brand)
    if request.method == "POST":
        Editform = forms.BrandForm(request.POST, instance=brand)

        if Editform.is_valid():
            Editform.save(commit=True)
            Editform = forms.BrandForm()
            updateText = 'Updated successfully'


    #title with brand
    name = brand.brandName
    #title with brand

    diction = {
        'title': name+' EDIT | CRUD',
        'Editform':Editform,
        'updateText':updateText
    }
    return render(request, 'crud_app/brand_editForm.html', context=diction)

def deleteBrand(request, id):

    brand = Brand.objects.get(pk=id).delete()
    deleteText = 'Deleted successfully'
    return index(request, deleteText)

def editProduct(request, id):
    updateText = 'no'
    productInfo = Product.objects.get(pk=id)
    productForm = forms.ProductForm(instance=productInfo)

    if request.method == "POST":
        productForm = forms.ProductForm(request.POST, instance=productInfo)
        if productForm.is_valid():
            productForm.save(commit=True)
            productForm = forms.ProductForm()
            updateText = 'Updated successfully'

    name = productInfo.productName
    diction = {
        'title': name+' EDIT | CRUD',
        'productForm':productForm,
        'updateText':updateText
    }
    return render(request, 'crud_app/edit_product.html', context=diction)

def deleteProduct(request, id):
    product = Product.objects.get(pk=id).delete()
    deleteText = 'Deleted successfully'
    return ProductView(request, deleteText)
