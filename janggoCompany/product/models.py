from django.db import models

# Create your models here.
class Product_type(models.Model):
    product_type = models.CharField(max_length=125)
    
    def __str__(self):
        return self.product_type

class Product_detail_type(models.Model):
    detail_type = models.CharField(max_length=125)

    product_type = models.ForeignKey(Product_type, on_delete = models.CASCADE)

    def __str__(self):
        return self.detail_type
    
class Product(models.Model):
    title = models.CharField(max_length=125, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    document = models.FileField(upload_to='documents/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    
    product_detail_type = models.ForeignKey(Product_detail_type, on_delete = models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
