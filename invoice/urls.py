from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewset, InvoiceViewset

router = DefaultRouter()
router.register(r'items', ItemViewset)
router.register(r'invoices', InvoiceViewset)

urlpatterns = [
    path('', include(router.urls)),
]
