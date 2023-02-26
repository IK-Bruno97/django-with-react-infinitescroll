from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import PostSerializers
from .models import Post

@api_view(['GET'])
def getData(request):
    post = Post.objects.all().order_by("-date")
    serializer = PostSerializers(post, many=True)
    return Response(serializer.data)

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-date")
    serializer_class = PostSerializers