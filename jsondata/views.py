from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import UploadedData
from .serializers import DataSerializer, GetFullUserSerializer, UserSerializerWithToken
# Create your views here.

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def data_list(request):
    data = UploadedData.objects.all()
    serializer = DataSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def set_list(request):
    data = request.data['body']
    serializer = DataSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201, safe=False)
    return JsonResponse(serializer.errors, status=400, safe=False)
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)

class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        user = request.data.get('user')
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializer = UserSerializerWithToken(data = user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})
        return Response({"response" : "success", "message" : "user created succesfully"})

