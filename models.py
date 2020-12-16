# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    idcart = models.IntegerField(db_column='idCart', primary_key=True)  # Field name made lowercase.
    customer_iduser = models.IntegerField(db_column='Customer_idUser')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class CartItems(models.Model):
    idcart_items = models.IntegerField(db_column='idCart_Items', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    cart_idcart = models.IntegerField(db_column='Cart_idCart')  # Field name made lowercase.
    cart_itemscol = models.CharField(db_column='Cart_Itemscol', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    product_idproduct = models.IntegerField(db_column='Product_idProduct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart_items'


class Customer(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    surname = models.CharField(db_column='Surname', max_length=45)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', max_length=45)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone number', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerOrder(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    customer_ordercol = models.CharField(db_column='customer ordercol', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    confirmation_number = models.IntegerField(db_column='confirmation number', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ordered_items = models.CharField(db_column='Ordered Items', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_city = models.CharField(db_column='Order city', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_zip = models.CharField(db_column='Order Zip', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_shipadress = models.CharField(db_column='Order ShipAdress', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_tax = models.FloatField(db_column='Order Tax', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_email = models.CharField(db_column='Order Email', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_iduser = models.IntegerField(db_column='Customer_idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer order'


class Product(models.Model):
    idproduct = models.IntegerField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imagesource = models.CharField(db_column='ImageSource', max_length=45, blank=True, null=True)  # Field name made lowercase.
    product_categories_categoryid = models.IntegerField(db_column='Product_categories_CategoryID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategories(models.Model):
    categoryid = models.IntegerField(db_column='CategoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_categories'


class Rating(models.Model):
    idrating = models.IntegerField(db_column='idRating', primary_key=True)  # Field name made lowercase.
    starrating = models.SmallIntegerField(db_column='StarRating', blank=True, null=True)  # Field name made lowercase.
    customer_iduser = models.IntegerField(db_column='Customer_idUser')  # Field name made lowercase.
    product_idproduct = models.IntegerField(db_column='Product_idProduct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rating'


class Transaction(models.Model):
    idtransaction = models.IntegerField(db_column='idTransaction', primary_key=True)  # Field name made lowercase.
    payment_method = models.CharField(db_column='Payment method', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    approvalstatus = models.CharField(db_column='ApprovalStatus', max_length=10)  # Field name made lowercase.
    delivery_time = models.DateField(db_column='Delivery time')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_order_id = models.IntegerField(db_column='customer order_id')  # Field renamed to remove unsuitable characters.
    product_idproduct = models.IntegerField(db_column='Product_idProduct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transaction'
