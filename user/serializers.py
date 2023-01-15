from rest_framework import serializers

from location.models import Location
from location.serializers import LocationPostSerializer
from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    total_ads = serializers.SerializerMethodField()

    def get_total_ads(self, obj):
        return obj.user_ad.filter(is_published=True).count()

    class Meta:
        model = User
        depth = 1
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = LocationPostSerializer()

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        for loc in self.location:
            location_obj, _ = Location.objects.get_or_create(
                name=loc
            )
            user.location.add(location_obj)
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    location = LocationPostSerializer(required=False)

    def is_valid(self, raise_exception=False):
        self.location_data = self.initial_data.pop('location', None)
        super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        for loc in self.location:
            location_obj, _ = Location.objects.get_or_create(
                name=loc
            )
            user.location.add(location_obj)
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
