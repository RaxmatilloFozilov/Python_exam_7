from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from app_report.models import PythonFramework, PythonLibrary, ProgrammingLanguage, PythonTopic
from app_report.permissions import MyPermission
from rest_framework import status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import DestroyAPIView, CreateAPIView, UpdateAPIView

from .serializers import PythonFrameworkSerializer, PythonTopicSerializer, PythonLibrarySerializer, \
    ProgrammingLanguageSerializer

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


class ProgrammingLanguageCreateViewSet(CreateAPIView):
    queryset = ProgrammingLanguage.objects
    serializer_class = ProgrammingLanguageSerializer
    permission_classes = [IsAdminUser]


class PythonFrameworkCreateViewSet(CreateAPIView):
    queryset = PythonFramework.objects
    serializer_class = PythonFrameworkSerializer
    permission_classes = [IsAdminUser]


class PythonLibraryCreateViewSet(CreateAPIView):
    queryset = PythonLibrary.objects
    serializer_class = PythonLibrarySerializer
    permission_classes = [IsAdminUser]


class PythonTopicCreateViewSet(CreateAPIView):
    queryset = PythonTopic.objects
    serializer_class = PythonTopicSerializer
    permission_classes = [IsAdminUser]


class ProgrammingLanguageUpdateViewSet(UpdateAPIView):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer
    permission_classes = [IsAdminUser]

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().patch(request, *args, **kwargs)


class PythonFrameworkUpdateViewSet(UpdateAPIView):
    queryset = PythonFramework.objects.all()
    serializer_class = PythonFrameworkSerializer
    permission_classes = [IsAdminUser]


class PythonLibraryUpdateViewSet(UpdateAPIView):
    queryset = PythonLibrary.objects.all()
    serializer_class = PythonLibrarySerializer
    permission_classes = [IsAdminUser]


class PythonTopicUpdateViewSet(UpdateAPIView):
    queryset = PythonTopic.objects.all()
    serializer_class = PythonTopicSerializer
    permission_classes = [IsAdminUser]


class ProgrammingLanguageDeleteViewSet(DestroyAPIView):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        self.object.delete()
        return Response()


class PythonFrameworkDeleteViewSet(DestroyAPIView):
    queryset = PythonFramework.objects
    serializer_class = PythonFrameworkSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        self.object.delete
        return Response()


class PythonLibraryDeleteViewSet(DestroyAPIView):
    queryset = PythonLibrary.objects
    serializer_class = PythonLibrarySerializer
    permission_classes = [IsAdminUser]

    def delete(self, *args, **kwargs):
        return Response()


class PythonTopicDeleteViewSet(DestroyAPIView):
    queryset = PythonTopic.objects
    serializer_class = PythonTopicSerializer
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return Response()