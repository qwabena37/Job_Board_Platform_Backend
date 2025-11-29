from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import IndustryViewSet, LocationViewSet, CompanyViewSet, JobViewSet

router = DefaultRouter()
router.register("industries", IndustryViewSet, basename="industry")
router.register("locations", LocationViewSet, basename="location")
router.register("companies", CompanyViewSet, basename="company")
router.register("", JobViewSet, basename="jobs")

urlpatterns = [path("", include(router.urls))]
