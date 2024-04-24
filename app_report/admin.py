from django.contrib import admin
from .models import PythonFramework,PythonLibrary,ProgrammingLanguage,PythonTopic
#
#
# class PythonFrameworkAdmin(admin.ModelAdmin):
#     list_display = ('id','name','creation_time','author')
#     search_fields = 'creation_time'
#
#
admin.site.register(PythonFramework)
admin.site.register(PythonLibrary)
admin.site.register(ProgrammingLanguage)
admin.site.register(PythonTopic)

