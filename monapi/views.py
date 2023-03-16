from django.shortcuts import render
from .models import Commentaire
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import * 
# Create your views here.

class CommentlistAPIView(APIView):
    def get (self, request, *arg, **kwargs):
        clist = Commentaire.objects.all(id=id)
        serializer = CommentaireSerializer(clist,many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post (self, request, *args, **kwargs):
        data = { 
            'titre': request.data.get('titre'),
            'commentaire': request.data.get('commntaire'),
            'cdate': request.data.get('cdate'),
        }
        serializer = Commentaire.Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'res':'error'}, status=status.HTTP_400_BAD_REQUEST)
    
class CommentdetailAPIView(APIView):
    def get (self, request, *args, **kwargs):
        Comment = Commentaire.objects.get(id=id)
        if Commentaire is None : 
            return Response({'res':'object not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = Comment.Serializer(Commentaire)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete (self, request,id):
        comment = Commentaire.objects.get(id=id)
        if comment is None:
            return Response({"res", "not found"}, status=status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response ({'res', "object delete"}, status=status.HTTP_200_OK)
        
    