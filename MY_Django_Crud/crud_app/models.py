from django.db import models

# Create your models here.
class Brand(models.Model):
    brandName = models.CharField(max_length = 50)
    brandOwnerName = models.CharField(max_length = 50)
    brandMobileNumber = models.CharField(max_length = 50)
    brandMainAddress = models.CharField(max_length = 50)

    def __str__(self):
        return self.brandName+" "+self.brandOwnerName+" "+self.brandMobileNumber+" "+self.brandMainAddress

class Product(models.Model):
    availability = (
        (1, "Yes"),
        (0, 'No')
    )

    proudctBrand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    productName = models.CharField(max_length = 50)
    productPrice = models.CharField(max_length = 50)
    productSize = models.CharField(max_length = 50)
    productAvailability = models.IntegerField(choices=availability)

    def __str__(self):
        return self.productName+" "+self.productPrice+" "+self.productSize+" "+str(self.productAvailability)
