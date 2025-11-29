from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import IndustryViewSet, LocationViewSet, CompanyViewSet, JobViewSet

router = DefaultRouter()
router.register("industries", IndustryViewSet)
router.register("locations", LocationViewSet)
router.register("companies", CompanyViewSet)
router.register("", JobViewSet)

urlpatterns = [path("", include(router.urls))]
