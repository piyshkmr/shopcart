from django.db import models

# Create your models here.


Categories = [
    ('Fashion', 'Fashion'),
    ('Electronics', 'Electronics'),
    ('Education', 'Education'),
    ('Essentials', 'Essentials'),
]


orderStatus = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Dispatched', 'Dispatched'),
    ('On The Way', 'On The Way'),
    ('Out For Delivery', 'Out For Delivery'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
]


class Product(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to="shop/images", default="")
    category = models.CharField(max_length=50, choices=Categories)
    subCategory = models.CharField(max_length=50)
    price = models.IntegerField()
    createdAt = models.DateField()

    def __str__(self):
        return f"{self.name}-{self.id}"


class Cart(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}-{self.id}"


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=15, default="")
    message = models.CharField(max_length=200, default="")

    def __str__(self):
        return f"{self.name}-{self.id}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, )
    email = models.CharField(max_length=30, )
    phone = models.CharField(max_length=15,)
    address = models.CharField(max_length=200, default="")
    items = models.CharField(max_length=1000, default="")
    state = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=80, default="")
    orderedDate = models.DateField(auto_now_add=True)
    totalAmount = models.IntegerField(default=0)
    status = models.CharField(
        max_length=80, choices=orderStatus, default="Pending")

    def __str__(self):
        return f"{self.name}-{self.id}"
