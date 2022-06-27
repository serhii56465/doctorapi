from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from doctor.models import Doctor, Area
from doctor.serializers import (
    DoctorSerializer,
    DoctorListSerializer,
    DoctorDetailSerializer,
    AreaSerializer,
)


class OrderPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 100


class DoctorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = (
        Doctor.objects.all()
        .prefetch_related("areas")
        .order_by("birthday", "experience")
    )
    serializer_class = DoctorSerializer
    pagination_class = OrderPagination
    lookup_field = "slug"

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Retrieve the doctors with filters"""
        experience = self.request.query_params.get("experience")
        areas = self.request.query_params.get("areas")

        queryset = self.queryset

        if experience:
            queryset = queryset.filter(experience__gte=experience)

        if areas:
            areas_ids = self._params_to_ints(areas)
            queryset = queryset.filter(areas__id__in=areas_ids)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return DoctorListSerializer

        if self.action == "retrieve":
            return DoctorDetailSerializer

        return DoctorSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "areas",
                type={"type": "list", "items": {"type": "number"}},
                description="Filter by area id (ex. ?areas=2,5)",
            ),
            OpenApiParameter(
                "experience",
                type=OpenApiTypes.INT,
                description="Filter by doctor experience (ex. ?experience=2)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class AreaViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
