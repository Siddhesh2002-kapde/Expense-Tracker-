from django.shortcuts import render
from expense_tracker.models import *
from rest_framework import viewsets,permissions
from expense_tracker.serializers import * 
from rest_framework.decorators import action
from django.db.models import Sum
from django.utils.timezone import now
from rest_framework.response import Response

class CategoryView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers  

class ExpenseView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializers  

    @action(detail = False,methods=['get'],url_path="monthly-summary")
    def monthly_summery(self,request):
        user = request.user
        today = now().date()
        first_day_of_month = today.replace(day=1)
        expense_monthly = Expense.objects.filter(user = user, date__gte = first_day_of_month, date__lte = today).values('category__name').annotate(total_sum = Sum('amount')).order_by("category__name")

        return Response(expense_monthly)


class PaymentTermView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializers  

class RecurringTypeView(viewsets.ModelViewSet):
    queryset = RecurringType.objects.all()
    serializer_class = RecurringTypeSerializers  

class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers  