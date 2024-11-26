from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework import status
from .models import Article, Comment
from products.models import DepositProducts, SavingProducts
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, DepositCommentSerializer, SavingCommentSerializer
from django.shortcuts import get_object_or_404, get_list_or_404 # type: ignore


# Create your views here.
# @authentication_classes([TokenAuthentication, BasicAuthentication])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST', 'GET'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def deposit_comment_create(request, deposit_pk):
    deposit_products = get_object_or_404(DepositProducts, pk=deposit_pk)
    if request.method == 'POST':
        serializer = DepositCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(deposit_products=deposit_products, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = deposit_products.comments.all()
        serializer = DepositCommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['POST', 'GET'])
def saving_comment_create(request, saving_pk):
    saving_products = get_object_or_404(SavingProducts, pk=saving_pk)
    if request.method == 'POST':
        serializer = SavingCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(saving_products=saving_products, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = saving_products.comments.all()
        serializer = SavingCommentSerializer(comments, many=True)
        return Response(serializer.data)
    