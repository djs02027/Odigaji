from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer, UserProfileSerializer

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
# 회원가입시는 인증 x 
def signup(request):
    # 사용자에게 요청으로 넘어온 패스워드 데이터 받기
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')

    # 패스워드와 확인용 패스워드 일치 여부 검사
    if password != passwordConfirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 아이디 일치여부 검사
    if User.objects.filter(username=request.data.get('username')).exists():
        return Response({'error': '이미 존재하는 아이디입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 닉네임 일치여부 검사
    if User.objects.filter(nickname=request.data.get('nickname')).exists():
        return Response({'error': '이미 존재하는 별명입니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # UserSerializer를 통해 사용자가 넘겨준 데이터 직렬화
    serializer = UserSerializer(data=request.data)

    # validation (password도 같이 직렬화)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # password 해싱 -> password -> 문자열 데이터로, set_password 메서드는 User 객체 저장 x 
        user.set_password(request.data.get('password'))
        # 유저 객체 저장
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def profile(request):
    # profile 조회
    if request.method == 'GET':
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    # profile 수정
    elif request.method == 'PUT':

        # profile 이미지 받기
        photo = request.data.get('photo')
        print(photo)

        # 별명 수정 시 일치여부 검사
        if request.user.nickname != request.data.get('nickname') and User.objects.filter(nickname=request.data.get('nickname')).exists():
            return Response({'error': '이미 존재하는 별명입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        
        serializer = UserProfileSerializer(request.user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('serializer is valid!')
            serializer.save(photo=photo)
            return Response(serializer.data)
        else:
            print('is not valid')
    
    # 회원탈퇴
    elif request.method == 'DELETE':
        user_pk = request.user.pk
        request.user.delete()
        return Response({ 'delete': f'{user_pk}번 회원이 탈퇴했습니다.' }, status=status.HTTP_204_NO_CONTENT)
