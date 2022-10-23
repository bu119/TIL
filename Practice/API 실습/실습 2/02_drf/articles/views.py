from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ArticleListSerializer, ArticleSerializer

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Article


@api_view(['GET', 'POST'])
def article_list(request):
    articles = get_list_or_404(Article)
    if request.method == 'GET':
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        context = {
            'delete': f'{article_pk}번 게시물이 삭제되었습니다.'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    

