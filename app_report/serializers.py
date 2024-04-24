from rest_framework import serializers
# from urllib3 import Url

from app_report.models import PythonFramework, PythonLibrary, ProgrammingLanguage, PythonTopic


class PythonFrameworkSerializer(serializers.ModelSerializer):
    python_detail_url = serializers.SerializerMethodField(read_only=True, source='get_python_detail_url')

    class Meta:
        model = PythonFramework
        fields = '__all__'
        depth = 1


class PythonLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonLibrary
        fields = ['name', 'creation_time', 'author', 'detailed_information']
        depth = 1


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = '__all__'
        depth = 1


class PythonTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonTopic
        fields = '__all__'
        depth = 1


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)



