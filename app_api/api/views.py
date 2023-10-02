from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from app_api.api.serializers import RegistrationSerializer
from app_api.models import Post_detail,Follower


@api_view(['POST'])
def logout_view(request):
    if request.method =='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view(request):
    if request.method =="POST":
        serializer =RegistrationSerializer(data =request.data)
        data ={}
        if serializer.is_valid():
            account =serializer.save()
            return serializer.save()
            data['response'] ='Registration Successfully'
            data ['username'] =account.username



