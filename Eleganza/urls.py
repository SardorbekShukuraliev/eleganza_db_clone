# from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import CategoryViewSet, ProductViewSet
from api.views import *
from rest_framework.routers import DefaultRouter 
# from rest_framework_simplejwt.views import TokenVerifyView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
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
    path('api/', include(router.urls)),  # ✅ Оставляем только API без токенов
]

