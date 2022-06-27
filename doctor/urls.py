from django.urls import path, include
from rest_framework import routers

from doctor.views import DoctorViewSet, AreaViewSet

router = routers.DefaultRouter()
router.register("doctors", DoctorViewSet)
router.register("areas", AreaViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "doctor"
