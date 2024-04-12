from django.urls import path
from .views import *
from rest_framework.authtoken import views
from app1.viewsets import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'viewset_category',CategoryModelViewset,basename='viewset_category')


urlpatterns = [
   
    path("category/",  CategoryView.as_view()),
    path("category/<int:id>/",  CategoryView.as_view()),
    path("product/", ProductView.as_view()),
    path("product/<int:id>/", ProductView.as_view()),
    path("purchase/", PurchaseView.as_view()),
    path("purchase/<int:id>/", PurchaseView.as_view()),
    path("sales/", SalesView.as_view()),
    path("sales/<int:id>/", SalesView.as_view()),
    path("stock/", StockView.as_view()),
    path("stock/<int:id>/", StockView.as_view()),
    path("login/", LoginView.as_view()),
    path("get-api-token/", views.obtain_auth_token),



]+router.urls