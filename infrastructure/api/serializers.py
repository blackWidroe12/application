from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from infrastructure.models.spatial import Infrastructure, Road, Building
from infrastructure.models.user import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'wards', 'last_location', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        wards = validated_data.pop('wards', [])
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        user.wards.set(wards)
        return user

class InfrastructureSerializer(GeoFeatureModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    ward = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Infrastructure
        geo_field = 'geom'
        fields = [
            'id', 'name', 'type', 'ward', 'status',
            'created_at', 'updated_at', 'last_inspected',
            'metadata'
        ]
        read_only_fields = ['created_at', 'updated_at']

class RoadSerializer(InfrastructureSerializer):
    class Meta(InfrastructureSerializer.Meta):
        model = Road
        fields = InfrastructureSerializer.Meta.fields + [
            'length_km', 'surface_type', 'road_class', 'lanes'
        ]

class BuildingSerializer(InfrastructureSerializer):
    class Meta(InfrastructureSerializer.Meta):
        model = Building
        fields = InfrastructureSerializer.Meta.fields + [
            'building_type', 'floor_count', 'capacity'
        ]

class WardGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        from infrastructure.models.core import Ward
        model = Ward
        geo_field = 'boundary'
        fields = ['id', 'name', 'code', 'population']