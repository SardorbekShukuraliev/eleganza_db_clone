from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import * 

router = DefaultRouter()
router.register(r'deliveries', DeliveryViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'payroll', PayrollViewSet)
router.register(r'suppliers', SuppliersViewSet)
router.register(r'transport', TransportViewSet)
router.register(r'shipment', ShipmentViewSet)
router.register(r'accessories', AccessoriesViewSet)
router.register(r'finance', FinanceViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'income', IncomeViewSet)
router.register(r'expenses', ExpensesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
