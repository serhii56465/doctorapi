from rest_framework import serializers

from doctor.models import Doctor, Area
from doctor_service.settings import BASE_URL


class DoctorSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = (
            "id",
            "name",
            "description",
            "slug",
            "areas",
            "birthday",
            "detail_url",
            "experience",
        )
        lookup_field = "slug"


class DoctorListSerializer(DoctorSerializer):
    areas = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    @staticmethod
    def get_detail_url(obj):
        return "{}/api/doctor/doctors/{}/".format(BASE_URL, obj.slug)


class DoctorDetailSerializer(DoctorSerializer):
    areas = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    @staticmethod
    def get_detail_url(obj):
        return "{}/api/doctor/doctors/{}/".format(BASE_URL, obj.slug)


class AreaSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Area
        fields = (
            "id",
            "name",
            "slug",
            "detail_url",
        )
        lookup_field = "slug"

    @staticmethod
    def get_detail_url(obj):
        return "{}/api/doctor/areas/{}/".format(BASE_URL, obj.slug)
