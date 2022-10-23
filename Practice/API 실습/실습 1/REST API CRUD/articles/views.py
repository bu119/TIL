
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

# 전체 조회 (QuerySet)
# DRF에서는 Respons로 응답
# DRF에서는 데코레이터 필수 (4가지 method 중 어떤 것을 허용할 지 쓴다.)
# @api_view() 를 비워두면 GET이 기본 값 (명시하는 것이 좋다.)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        context = {
            'delete': f'{article_pk}번 삭제 성공'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer= ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)