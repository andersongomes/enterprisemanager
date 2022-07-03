from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id_updater = models.IntegerField()
    updated_at = models.DateTimeField()


class Address(models.Model):
    country = models.CharField(max_length=2)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    address_number = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=50)


class Provider(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    identifier = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="provider_address")


class Client(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    identifier = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="client_address")


class Buy(models.Model):
    buy_value = models.DecimalField()
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT, related_name="buy_provider")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="buy_user")
    created_at = models.DateTimeField(auto_now_add=True)


class Lot(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.PROTECT, related_name="lot_buy")
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="lot_product")
    quantity = models.DecimalField()
    quantity_consumed = models.DecimalField()
    expiration_date = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    purchase_value = models.DecimalField()


class Sale(models.Model):
    sale_value = models.DecimalField()
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="sale_client")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="sale_user")
    created_at = models.DateTimeField(auto_now_add=True)


class SaleLot(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT, related_name="salelot_sale")
    lot = models.ForeignKey(Lot, on_delete=models.PROTECT, related_name="salelot_lot")
    sale_lot_value = models.DecimalField()
    quantity = models.DecimalField()
