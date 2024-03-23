from api.views import UserProfileViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'user', UserViewSet, basename="user")
router.register(r'profile', UserProfileViewSet, basename="profile")
urlpatterns = [
    
]+router.urls