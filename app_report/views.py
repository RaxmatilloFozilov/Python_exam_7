from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from app_report.models import PythonFramework, PythonLibrary, ProgrammingLanguage, PythonTopic
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

