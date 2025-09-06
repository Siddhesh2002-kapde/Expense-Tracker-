from django.db import models
from django.contrib.auth import get_user_model 
# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name 

class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="expenses"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses"
    )
    payment_term = models.ForeignKey(
        'PaymentTerm',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses"
    )
    recurring_type = models.ForeignKey(
        'RecurringType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses"
    )
    currency = models.ForeignKey(
        'Currency',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="expenses"
    )
    title = models.CharField(max_length=200)  
    description = models.TextField(blank=True) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)     

    class Meta:
        db_table = 'expenses'
        ordering = ["-date", "-created_at"]


class PaymentTerm(models.Model):
    payment_term_name = models.CharField(max_length=50)  
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="payment_terms"
    )

    class Meta:
        db_table = 'payment_terms'
        unique_together = ("payment_term_name", "user")

    def __str__(self):
        return f"{self.payment_term_name} ({self.user})"
    

class RecurringType(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'recurring_type'

    def __str__(self):
        return f"{self.name}"


class Currency(models.Model):
    code = models.CharField(max_length=10)  
    symbol = models.CharField(max_length=5, blank=True) 

    class Meta:
        db_table = 'currency'

    def __str__(self):
        return f"{self.code} {self.symbol}"
    
