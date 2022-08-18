from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import User
from album.models import Artist
from .serializers import UserSerializer

# 회원가입
class Signup(APIView):
     def post(self, request):

        # 이미 가입한 email인 경우
        if User.objects.filter(userEmail=request.data['userEmail']):
            return Response({"message": "이미 있는 email"}, status=409)
        
        # password1이랑 password2가 일치
        elif request.data["password1"] == request.data["password2"]:
            user = User.objects.create_user(
                userEmail = request.data["userEmail"],
                userName = request.data["userName"],
                password = request.data["password1"]
            )
            #auth.login(request, user)   
            return Response({"message": "Success signup"}, status=201)

       


#로그인

class Login(APIView):
    def post(self, request, *args, **kwargs):
        userEmail = request.data["userEmail"]
        pwd = request.data["password"]

        user = auth.authenticate(userEmail=userEmail, password=pwd)

        # 유저 정보 확인
        if user is not None:
            auth.login(request, user)
            print(request.user)
            return Response({"id": user.id}, status=200)
        
        # 가입하지 않은 유저인 경우
        else:
            return Response({"message": "유저 정보가 없음"}, status=404)

# 내 정보 보기, 내 정보 수정
class userinfo(APIView):
    def get(self, request):
        user = request.user
        data = User.objects.filter(id=user.id)
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)

    def patch(self, request):
        user=request.user
        data=User.objects.filter(id=user.id)
        serializer = UserSerializer(data, many=True)
        
        user.userName=request.data['userName']
        user.userEmail=request.data['userEmail']
        if request.data["password1"] != request.data["password2"]:
            return Response({
                "message": "비밀번호가 다릅니다"
            })
        else:
            user.set_password(request.data["password1"])
        user.save()
        return Response(serializer.data)

#로그아웃
def Logout(self, request):
    auth.logout(request)
    return Response({"message": "Success Logout"}, status=200)


#참고한 코드(이후에도 사용 예정)

''''
class login(APIView):
    def post(self, request, *args, **kwargs):
        userEmail = request.data["email"]
        pwd = request.data["password"]

        user = auth.authenticate(email=userEmail, password=pwd)

        # 유저 정보 확인
        if user is not None:
            auth.login(request, user)
            return Response({"id": user.id}, status=200)
        
        # 가입하지 않은 유저인 경우
        else:
            return Response({"message": "유저 정보가 없음"}, status=404)


# 로그아웃 이게 맞습니다
def logout(request):
    auth.logout(request)
    return Response({"message": "Success Logout"}, status=200)

class signup(APIView):
    def post(self, request, *args, **kwargs):

        # 이미 가입한 email인 경우
        if User.objects.filter(email=request.data['email']):
            return Response({"message": "이미 있는 email"}, status=409)
        
        # password1이랑 password2가 일치
        elif request.data["password1"] == request.data["password2"]:
            user = User.objects.create_user(
                email = request.data["email"],
                nickname = request.data["nickname"],
                password = request.data["password1"]
            )
            #auth.login(request, user)   
            return Response({"message": "Success signup"}, status=201)

        # 불일치
        elif request.data["password1"] != request.data["password2"]:
            return Response({"message": "password가 일치하지 않음!!"}, status=400)

class account_API(APIView):
    def get(self, request, userId):
        user = User.objects.get(id=userId)
        serializer = accountSerializers(user)
        return Response(serializer.data, status=200)

    def patch(self, request, userId):
        user = get_object_or_404(User, id=userId)
        user.user_color = request.data["user_color"]
        user.save()
        return Response(user.user_color)
 '''


# 아티스트 구독, 삭제
class SubArtist(APIView):
    def patch(self, request):
        # print(request.data) # {'artists': ['아이브', '에스파']}

        # request.data의 'artists'에 담긴 리스트를 순회하며 'req_artist' 리스트에 추가
        req_artist=[]
        artist_len=len(request.data['artists'])
        for i in range(artist_len): req_artist.append(request.data['artists'][i])
        print(req_artist)
        
        user=request.user
        for artist_id in req_artist:
            artist=get_object_or_404(Artist, pk = artist_id)
            user.userSubartist_type_List.add(artist)
            print(user.userSubartist_type_List)
        user.save()

        return Response({
            "message" : "관심 아티스트 구독이 완료되었어요!"
        })
        
    def delete(self, request):
        req_artist=[]
        artist_len=len(request.data['artists'])
        for i in range(artist_len): req_artist.append(request.data['artists'][i])
        print(req_artist)
        
        user=request.user
        for artist_id in req_artist:
            artist=get_object_or_404(Artist, pk = artist_id)
            user.userSubartist_type_List.remove(artist)
            print(user.userSubartist_type_List)
        user.save()

        return Response({
            "message" : "관심 아티스트가 삭제되었습니다."
        })