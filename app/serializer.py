from rest_framework import serializers
from .models import Post,Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','description','pub_date')

class CommentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="title.title", read_only=True)
    def get_queryset(self):
        return Comment.objects.all().prefetch_related("title")
    class Meta:
        model = Comment
        fields = ('title','comments')
