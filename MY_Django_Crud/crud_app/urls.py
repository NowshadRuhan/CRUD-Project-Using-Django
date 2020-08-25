from django.conf.urls import url
from django.urls import path
from crud_app import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='home'),
    path('product_view/', views.ProductView, name='product_view'),
    path('brand_product/<int:proudctBrand_id>/', views.BrandProduct, name='brand_product'),
    path('brand_edit/<int:id>/', views.editBrand, name='brand_edit'),
    path('brand_delete/<int:id>/', views.deleteBrand, name='brand_delete'),
    path('edit_product/<int:id>/', views.editProduct, name='edit_product'),
    path('product_delete/<int:id>/', views.deleteProduct, name='product_delete')
]
