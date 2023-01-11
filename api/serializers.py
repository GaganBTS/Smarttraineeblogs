from rest_framework import serializers
from blogs.models import Post,Tag,Author
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False)
    tag = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'
