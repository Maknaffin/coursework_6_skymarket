from rest_framework import serializers

from .models import Ad, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("text",)


class CommentListSerializer(serializers.ModelSerializer):
    author_id = serializers.CharField(source="author.id")
    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")
    author_image = serializers.ImageField(source="author.image")

    class Meta:
        model = Comment
        fields = (
            "pk",
            "text",
            "author_id",
            "created_at",
            "author_first_name",
            "author_last_name",
            "ad_id",
            "author_image",
        )


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description')


class AdListSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source="author.phone")
    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")
    author_id = serializers.CharField(source="author.id")

    class Meta:
        model = Ad
        fields = (
            "pk",
            "image",
            "title",
            "price",
            "phone",
            "description",
            "author_first_name",
            "author_last_name",
            "author_id",
        )
