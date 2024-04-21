from rest_framework import serializers
# from urllib3 import Url

from app_report.models import PythonFramework, PythonLibrary, ProgrammingLanguage, PythonTopic


class PythonFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonFramework
        fields = '__all__'


class PythonLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonLibrary
        fields = '__all__'


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = '__all__'


class PythonTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonTopic
        fields = '__all__'



class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)