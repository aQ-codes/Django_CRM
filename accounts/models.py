from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 200, null = True) #no error when no name
    phone = models.CharField(max_length = 200,null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null =True)  #snap the item when the item is created

    def __str__(self):  
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True) 
   
    def __str__(self):  
        return self.name

    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        )
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True) 
    tags = models.ManyToManyField(Tag)

    def __str__(self):  
        return self.name





class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery' ),
        ('Delivered', 'Delivered' ),

        )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL) 
    #a dropdown will be created
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True) 
    #status of delivery and  is dropdown .
    status = models.CharField(max_length = 200, null = True, choices=STATUS) #choices refer to STATUS
    note = models.CharField(max_length = 200, null = True)
    
    def __str__(self):  
        return self.product.name
  
     
