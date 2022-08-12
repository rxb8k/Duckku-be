from django.shortcuts import render
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import User

# 회원가입
class Signup(APIView):
    def post(self, request, *args, **kwargs):
       
            return Response(status=400)


#로그인
class Login(APIView):
    def post(self, request, *args, **kwargs):
       
        return

#로그아웃
class Logout(APIVeiw):
    def post(self, request):
        return
