from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

#---  --- this allows the customer account to show the actual name
    #instead of customer1, customer2
    def __str__(self):
        return self.name

class Tag(models.Model): #for creating tags
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (('Small','Small'),
                  ('Medium', 'Medium'),
                  ('Large', 'Large'),
                )


    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    tag = models.ManyToManyField(Tag) #relationship between product and tags

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS =(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

#____relationship____

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    #foreign key gets the list of customers created from customer class
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name


