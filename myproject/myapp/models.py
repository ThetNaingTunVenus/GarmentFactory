from django.db import models

# Create your models here.
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    Vendor = models.CharField(max_length=225, blank=True, null=True)
    BuyerName = models.CharField(max_length=225)
    Address = models.CharField(max_length=225)
    def __str__(self):
        return self.BuyerName

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    Vendor = models.CharField(max_length=225, blank=True, null=True)
    BuyerName = models.CharField(max_length=225)
    StyleCode = models.CharField(max_length=225,unique=True)
    ItemName = models.CharField(max_length=225,blank=True,null=True)
    barcode = models.CharField(max_length=225, blank=True,null=True)
    def __str__(self):
        return self.StyleCode

class ProductionLine(models.Model):
    id = models.AutoField(primary_key=True)
    ProductionLine = models.CharField(max_length=255)

    def __str__(self):
        return self.ProductionLine

class OrderQty(models.Model):
    buyer = models.CharField(max_length=255)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    style = models.CharField(max_length=255)
    item = models.CharField(max_length=255, blank=True, null=True)
    order_qty = models.PositiveIntegerField(default=0)
    cmp = models.FloatField()
    cmp_amount = models.FloatField()
    making_charge = models.PositiveIntegerField(default=0)
    import_export_charge = models.PositiveIntegerField(default=0)
    box_charge = models.PositiveIntegerField(default=0)
    poly_bag = models.PositiveIntegerField(default=0)
    sewing_thread = models.PositiveIntegerField(default=0)
    cmp_condition = models.FloatField()
    date = models.DateField()
    serial_number = models.CharField(max_length=255)
    md_charge = models.CharField(max_length=255,blank=True,null=True)
    delivery = models.DateField(blank=True,null=True)
    fabricETA = models.DateField(blank=True,null=True)
    accETA = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.style

class ProductionInput(models.Model):
    line = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    input_qty = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.line