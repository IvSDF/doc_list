from rest_framework import serializers

from .models import Doctor, Direction


class DirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direction
        fields = ('title', 'slug', 'sort_number')


class DoctorSerializer(serializers.ModelSerializer):
    directions = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = ('title', 'directions', 'slug', 'birthday', 'years_of_experience')


class DocItemSerializer(serializers.ModelSerializer):
    directions = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Doctor
        exclude = ('sort_number',)
