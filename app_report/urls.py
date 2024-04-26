from django.urls import path

from rest_framework.routers import DefaultRouter


from .views import (
    ProgrammingLanguageViewSet, ProgrammingLanguageCreateViewSet, ProgrammingLanguageUpdateViewSet,
    ProgrammingLanguageDeleteViewSet,
    PythonLibraryViewSet,
    PythonFrameworkViewSet,
    PythonTopicViewSet,
)


router = DefaultRouter()
router.register(r'programming_language',ProgrammingLanguageViewSet)
router.register(r'frameworks', PythonFrameworkViewSet)
router.register(r'topics', PythonTopicViewSet)
router.register(r'libraries', PythonLibraryViewSet)


urlpatterns = [
    path('create/', ProgrammingLanguageCreateViewSet.as_view()),
    path('update/<int:pk>/', ProgrammingLanguageUpdateViewSet.as_view()),
    path('delete/<int:pk>/', ProgrammingLanguageDeleteViewSet.as_view()),

] + router.urls
