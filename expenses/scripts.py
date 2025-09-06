import os
import django

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expenses.settings")

# Setup Django
django.setup()

from django.contrib.auth import get_user_model
from expense_tracker.models import Category, Expense, PaymentTerm, RecurringType, Currency
from faker import Faker
from django.db import transaction
# Now you can use ORM here
User = get_user_model()
fake = Faker('en_IN')

data = range(10)

users = []
for _ in range(5):
    user = User(    
    email=fake.email()[:100],            
    first_name=fake.first_name()[:30],   
    last_name=fake.last_name()[:30],     
    phone_number=fake.phone_number()[:12], 
    address_line_1=fake.address()[:100], 
    address_line_2=fake.street_address()[:100]
    )
    user.set_password("pass@123")
    user.save()

print("User Created Sucessfully!")

# user = User.objects.all()
# category = Category.objects.filter(user__id = 4)
# print("user_is-------------------",user)
# print("category_is-------------------",category)



