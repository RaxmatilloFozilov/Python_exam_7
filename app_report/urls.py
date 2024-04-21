from django.urls import path

from rest_framework.routers import DefaultRouter


from .views import (
    ProgrammingLanguageViewSet,
    PythonLibraryViewSet,
    PythonFrameworkViewSet,
    PythonTopicViewSet,

)

router = DefaultRouter()
router.register(r'programming_language',ProgrammingLanguageViewSet)
router.register(r'frameworks', PythonFrameworkViewSet)
router.register(r'topics', PythonTopicViewSet)
router.register(r'libraries', PythonLibraryViewSet)


urlpatterns = router.urls
