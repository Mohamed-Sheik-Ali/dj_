from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from rest_framework import status
from .serializer import UserSignUpSerializer

class UserSignupApiview(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    permission_classes = [AllowAny]

    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSignUpSerializer(queryset, many=True)
    #     return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"status": "failure", "data": serializer.errors})
