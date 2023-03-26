from django.contrib import admin
from app.models import Expenses

# Register your models here.
class ExpensesAdmin(admin.ModelAdmin):
    list_display= ('exp_date', 'exp_type', 'exp_description', 'exp_amount','exp_created','author')
    
  
admin.site.register(Expenses, ExpensesAdmin)
