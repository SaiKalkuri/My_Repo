from api2.views import ProxyUserProfileViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'proxyprofile', ProxyUserProfileViewSet, basename="proxyprofile")
urlpatterns = [
    
]+router.urls