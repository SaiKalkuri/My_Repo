from rest_framework import routers
from . import views
router=routers.DefaultRouter()
router.register('customer',views.CustomerView)
router.register('premium',views.PremiumView)
router.register('claims',views.ClaimsView)
router.register('expanses',views.ExpenseView)
router.register('result',views.Profit_loss, basename='result')
urlpatterns = [
]+router.urls


