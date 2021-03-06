from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '[ name: ' + self.name + ' phone: ' + self.phone + ' email: ' + self.email + ' ]'

class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '[ name: ' + self.name + ' ]'

class Product(models.Model):
    CATEGORY = (('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),)
    name = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '[ name: ' + self.name + ' price: ' + str(self.price) + \
               ' category: ' + self.category + ' tags: ' + str(self.tags) + ' ]'

class Order(models.Model):
    STATUS = (('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS)

    def __str__(self):
        return '[ customer name: ' + self.customer.name + ' productName: ' + \
               self.product.name + ' status: ' + self.status + ' ]'
