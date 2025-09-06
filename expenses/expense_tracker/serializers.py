from rest_framework.serializers import ModelSerializer 
from expense_tracker.models import *

class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseSerializers(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class PaymentTermSerializers(ModelSerializer):
    class Meta:
        model = PaymentTerm
        fields = '__all__'

class RecurringTypeSerializers(ModelSerializer):
    class Meta:
        model = RecurringType
        fields = '__all__'

class CurrencySerializers(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'