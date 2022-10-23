from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

from music import serializers
from . models import Music

@api_view(['GET', 'POST'])
def music_list(request):
    musics = get_list_or_404(Music)
    if request.method == 'GET':
        serializer = serializers.MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = serializers.MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializer = serializers.MusicSerializer(music)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = serializers.MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        music.delete()
        context = {
            'delete': f'음악 {music_pk}번이 삭제되었습니다.'
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)