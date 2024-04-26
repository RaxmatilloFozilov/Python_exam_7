from django.urls import path, include

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
    # path('api/v1/programming_language/', include('routing.urls')),
    path('create/', ProgrammingLanguageCreateViewSet.as_view()),
    path('update/<int:pk>/', ProgrammingLanguageUpdateViewSet.as_view()),
    path('delete/<int:pk>/', ProgrammingLanguageDeleteViewSet.as_view()),

    # path('create/', PythonFrameworkCreateViewSet.as_view()),
    # path('update/<int:pk>/', PythonFrameworkUpdateViewSet.as_view()),
    # # path('delete/<int:pk>/', ),
    #
    # path('create/', PythonLibraryCreateViewSet.as_view()),
    # path('update/<int:pk>/', PythonLibraryUpdateViewSet.as_view()),
    # path('delete/<int:pk>/', PythonLibraryDeleteViewSet.as_view()),
    #
    # path('create/', PythonTopicCreateViewSet.as_view()),
    # path('update/<int:pk>/', PythonTopicUpdateViewSet.as_view()),
    # path('delete/<int:pk>/', PythonTopicDeleteViewSet.as_view()),

    # path('', include(router.urls)),

] + router.urls
