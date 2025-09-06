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
import sys
sys.stdout.reconfigure(encoding='utf-8')

data = range(10)

# users = []
# for _ in range(5):
#     user = User(    
#     email=fake.email()[:100],            
#     first_name=fake.first_name()[:30],   
#     last_name=fake.last_name()[:30],     
#     phone_number=fake.phone_number()[:12], 
#     address_line_1=fake.address()[:100], 
#     address_line_2=fake.street_address()[:100]
#     )
#     user.set_password("pass@123")
#     user.save()

# print("User Created Sucessfully!")

# user = User.objects.all()
# category = Category.objects.filter(user__id = 4)
# print("user_is-------------------",user)
# print("category_is-------------------",category)



user = User.objects.all()
category = Category.objects.filter(user__in = list(user))
payment_terms = PaymentTerm.objects.filter(user__in = list(user))
currency = Currency.objects.all()
recurring_type = RecurringType.objects.all()


print("user----------",user)
print("category----------",category)
print("payment_terms----------",payment_terms)
print("currency----------",currency)
print("recurring_type----------",recurring_type)


import random
import datetime

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2025, 9, 1)
expenses = []
with transaction.atomic():
    for i in range(50): 
        random_date = start_date + datetime.timedelta(
            days=random.randint(0, (end_date - start_date).days)
        )
        random_user = random.choice(user)
        random_category = Category.objects.filter(user = random_user)
        random_payment_terms = PaymentTerm.objects.filter(user = random_user)
        expenses.append(
            Expense(
                user=random_user,
                category=random.choice(list(random_category)),
                payment_term=random.choice(list(random_payment_terms)),
                recurring_type=random.choice(list(recurring_type)),
                currency=random.choice(list(currency)),
                title=f"Expense {i+1}",
                description="This is dummy expense data",
                amount=round(random.uniform(100, 5000), 2),
                date=random_date,
            )
        )
    Expense.objects.bulk_create(expenses)
    print("50 dummy expenses inserted successfully!")
