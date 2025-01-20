from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet,
    AccountViewSet,
    CategoryViewSet,
    CategoryDetailViewSet,
    TransactionViewSet,
    MonthlyViewSet,
)

router = DefaultRouter()
router.register(r"books", BookViewSet, basename="book")
router.register(r"accounts", AccountViewSet, basename="account")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"categorydetails", CategoryDetailViewSet, basename="categorydetail")
router.register(r"transactions", TransactionViewSet, basename="transaction")
router.register(r"monthly", MonthlyViewSet, basename="monthly")

urlpatterns = router.urls
