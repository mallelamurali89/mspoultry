from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expenses(models.Model):
    EXPENSES_TYPE_CHOICES = (('products','Products'),('hatching','Hatching'),('traveling','Traveling'),('chick_feed','Chick Feed'),('grower_feed','Grower Feed'),('layer_feed','Layer Feed'),('medicines','Medicines'),('workers','Workers'),('rent','Rent'),('others','Others'))

    exp_date = models.DateField(blank=True, null=True)
    exp_type = models.CharField(max_length=15,choices=EXPENSES_TYPE_CHOICES,default='others')
    exp_description = models.TextField(null=True,blank=True)
    exp_amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    exp_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='relatedUser',default="")
    class Meta:
        ordering=('-exp_created',) 