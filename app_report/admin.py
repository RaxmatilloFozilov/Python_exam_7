from django.contrib import admin
from .models import PythonFramework, PythonLibrary, ProgrammingLanguage, PythonTopic


admin.site.register(PythonFramework)
admin.site.register(PythonLibrary)
admin.site.register(ProgrammingLanguage)
admin.site.register(PythonTopic)

