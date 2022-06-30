from django.db import models

class InventoryModel(models.Model):
    toy_id= models.IntegerField(primary_key=True)
    toy_name= models.CharField(max_length=100)
    manufacturer_id= models.IntegerField()
    price= models.IntegerField()
    quantity= models.IntegerField()
    country= models.CharField(max_length=50)
    category= models.CharField(max_length=100)
    raw_material= models.CharField(max_length=100)
    color=models.CharField(max_length=30)
    class Meta:
        db_table= "Inventory"




