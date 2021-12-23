from django.http import request, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_auth.models import User
from .permissions import IsAdminUserForObject, IsStaffPermission, AuthorModifyOrReadOnly
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AuthorModifyOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user).order_by('-created_at')

    def create(self, request):
        user = self.request.user
        #user_id = User.objects.filter(username=user).values_list('pk', flat=True)
        new_post = Post.objects.create(author=user, title=request.data['title'], content=request.data['content'])
        new_post.save()
        return Response("new post")


class PostListView(viewsets.ViewSet):
    """
    Get all posts
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsStaffPermission]

    def list(self, request):
        posts = Post.objects.all().order_by('-created_at')
        serializer_posts = PostSerializer(posts, many=True).data
        return Response(serializer_posts)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Post.objects.get(pk=pk)
        serializer = PostSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Post.objects.get(pk=pk)
        queryset.delete()
        return Response('post was deleted')


class NewUser(viewsets.ViewSet):
    """
    Create user
    """

    pass


def get_ip(request):
    from django.http import HttpResponse
    return HttpResponse(request.META['REMOTE_ADDR'])


"""
def blog_list(request):
    if request.method == "GET":
        user = self.request.user
        posts = Post.objects.filter(author=user)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def post_blog(request, pk):
    user = self.request.user
    new_post = Post(author=user, title=request.data['title'], content=request.data['content'])
    new_post.save()
"""
