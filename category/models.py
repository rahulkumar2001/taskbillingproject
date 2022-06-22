from django.db import models

class Category(models.Model):
    restaurant=models.ForeignKey('Restaurant',on_delete=models.CASCADE,default="")
    items=models.CharField(max_length=30)
    food_name=models.CharField(max_length=40)


class Restaurant(models.Model):
     restaurant_name=models.CharField(max_length=40)
     description=models.CharField(max_length=40)
     total_table=models.CharField(max_length=50)

class order(models.Model):
    order_id=models.CharField(max_length=40)
    food_name=models.CharField(max_length=40)
    table_num=models.CharField(max_length=40)



    
