from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response

from blog.models import Comment
from blog.serializers import CommentListCreateSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListCreateSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ("text",)
    ordering_fields = ("created_at", "updated_at")
    filterset_fields = ("text", "author_id")
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        post_id = kwargs.get("post_id")
        queryset = queryset.filter(post_id=post_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        author_id = request.user.id
        post_id = kwargs.get("post_id")

        serializer.validated_data["author_id"] = author_id
        serializer.validated_data["post_id"] = post_id

        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
