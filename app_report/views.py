from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from app_report.models import PythonFramework, PythonLibrary, ProgrammingLanguage, PythonTopic, User
from app_report.permissions import MyPermission

from app_report.serializers import (
    PythonFrameworkSerializer,
    PythonTopicSerializer,
    PythonLibrarySerializer,
    ProgrammingLanguageSerializer
)


class ProgrammingLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer
    permission_classes = [IsAuthenticated]


class PythonFrameworkViewSet(viewsets.ModelViewSet):
    queryset = PythonFramework.objects.all()
    serializer_class = PythonFrameworkSerializer
    permission_classes = [IsAdminUser]


class PythonLibraryViewSet(viewsets.ModelViewSet):
    queryset = PythonLibrary.objects.all()
    serializer_class = PythonLibrarySerializer
    permission_classes = [IsAuthenticated]


class PythonTopicViewSet(viewsets.ModelViewSet):
    queryset = PythonTopic.objects.all()
    serializer_class = PythonTopicSerializer
    permission_classes = [IsAdminUser]


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            # Parolni o'zgartirish logikasi
            return Response("Parol muvaffaqiyatli o'zgartirildi", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            # Parolni tiklash logikasi
            return Response("Parolni tiklash uchun havola yuborildi", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Basseyn view lar uchun
class ExampleAPIView(APIView):
    def get(self, request):
        # Handle GET request
        data = {'message': 'This is a GET request.'}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # Handle POST request
        data = {'message': 'This is a POST request.'}
        return Response(data, status=status.HTTP_201_CREATED)