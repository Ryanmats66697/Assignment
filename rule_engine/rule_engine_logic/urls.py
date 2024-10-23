from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RuleViewSet, UserProfileViewSet, index  # Import index here

router = DefaultRouter()
router.register(r'rules', RuleViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', index, name='index'),  # Ensure the index view is accessible
    path('api/', include(router.urls)),  # Keep this line to include the router URLs
]
