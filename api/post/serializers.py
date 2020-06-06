from rest_framework import serializers

from main.models import Post


class CreatePostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = '__all__'


class LikePostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    created_at = serializers.DateTimeField(required=False)

