from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Category,PaymentTerm

User = get_user_model()
DEFAULT_CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Health",
    "Shopping",
    "Utilities",
    "Education",
    "Travel",
    "Salary",
    "Miscellaneous"
]

@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
    """Create default categories when a new user is registered"""
    if created: 
        for cat in DEFAULT_CATEGORIES:
            Category.objects.create(name=cat, user=instance)


DEFAULT_PAYMENT_TERMS = [
    'Cash','Credit Card','Debit Card','Net Banking','Check'
]
@receiver(post_save,sender = User)
def create_default_payment_terms(sender,instance,created,**kwargs):
    if created:
        for payment_terms in DEFAULT_PAYMENT_TERMS:
            PaymentTerm.objects.create(payment_term_name = payment_terms,user = instance)



