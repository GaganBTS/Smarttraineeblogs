from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.models import Post 
from .serializers import PostSerializer


@api_view(['GET'])
def getposts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)