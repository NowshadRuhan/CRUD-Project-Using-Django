from django import forms
from crud_app import models

class BrandForm(forms.ModelForm):

    brandName = forms.CharField(label='Brand Name ', widget=forms.TextInput(attrs={
    'placeholder':'Enter Brand Name','style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))
    brandOwnerName = forms.CharField(label='Brand Owner Name ', widget=forms.TextInput(attrs={
    'placeholder':'Enter Brand Owner Name', 'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))
    brandMobileNumber = forms.CharField(label='Mobile ', max_length=11, widget=forms.TextInput(attrs={
    'placeholder':'016', 'type':'number', 'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))
    brandMainAddress = forms.CharField(label='Address ', max_length=100, widget=forms.Textarea(attrs={
    'placeholder':'Enter you address',"rows":3, "cols":50,
    'style':'width:300px; height:43px; border: 1px solid gray; border-radius:2px;'
    }))

    class Meta:
        model = models.Brand
        fields = "__all__"


class ProductForm(forms.ModelForm):
    availability = (
        (1, "Yes"),
        (0, 'No')
    )

    productName = forms.CharField(label='Product Name ', widget=forms.TextInput(attrs={
    'placeholder':'Enter Product Name','style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))

    productPrice = forms.CharField(label='Price ', max_length=11, widget=forms.TextInput(attrs={
    'placeholder':'Product Price', 'type':'number',
    'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))

    productSize = forms.CharField(label='Size ', widget=forms.TextInput(attrs={
    'placeholder':'Product Size',
    'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
    }))

    productAvailability = forms.ChoiceField(label='Availability ',choices=availability,
     widget=forms.Select(attrs={
     'style':'width:300px; height:33px; border: 1px solid gray; border-radius:2px;'
     }))

    class Meta:
        model = models.Product
        fields = "__all__"
