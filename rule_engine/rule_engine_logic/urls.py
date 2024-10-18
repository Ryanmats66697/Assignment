from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RuleViewSet

router = DefaultRouter()
router.register(r'rules', RuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('evaluate/', RuleViewSet.as_view({'post': 'evaluate'}), name='evaluate'),
]
