# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expense_tracker.views import *

router = DefaultRouter()
router.register(r'categories', CategoryView, basename="categories")
router.register(r'expenses', ExpenseView, basename="expenses")
router.register(r'payment-terms', PaymentTermView, basename="payment-terms")
router.register(r'recurring-types', RecurringTypeView, basename="recurring-types")
router.register(r'currencies', CurrencyView, basename="currencies")

urlpatterns = [
    path('', include(router.urls)),
]
