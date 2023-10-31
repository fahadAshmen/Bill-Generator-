from django.db import models

class Bill(models.Model):
    bill_code = models.CharField(max_length=10)
    total = total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.bill_code
    
class BillItems(models.Model):
    bill_code = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bills',null=True,blank=True)
    item_name = models.CharField(max_length=155)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)