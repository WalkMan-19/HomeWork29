from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str
from rest_framework import serializers

from ads.models import Ad
from category.models import Category
from user.models import User


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=User.objects.all(),
        slug_field='username',
    )
    category = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Category.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self.category = self.initial_data.pop('category')
        return super(AdCreateSerializer, self).is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)
        for cat in self.category:
            category_obj, _ = Category.objects.get_or_create(
                name=cat
            )
            ad.category.add(category_obj)
        ad.save()
        return ad


class AdUpdateSerializer(serializers.ModelSerializer):
    author = author = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=User.objects.all(),
        slug_field='username',
    )
    category = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Category.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        self.category = self.initial_data.pop('category')
        return super(AdUpdateSerializer, self).is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()

        for cat in self.category:
            category_obj, _ = Category.objects.get_or_create(
                name=cat
            )
            ad.category.add(category_obj)
        ad.save()
        return ad


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]
