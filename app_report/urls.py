from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
    ProgrammingLanguageViewSet,
    PythonLibraryViewSet,
    PythonFrameworkViewSet,
    PythonTopicViewSet,
    ChangePasswordView,
    ResetPasswordView
)

router = DefaultRouter()
router.register(r'programming_language',ProgrammingLanguageViewSet)
router.register(r'frameworks', PythonFrameworkViewSet)
router.register(r'topics', PythonTopicViewSet)
router.register(r'libraries', PythonLibraryViewSet)
# router.register(r'change_password', ChangePasswordView)
# router.register(r'reset_password', ResetPasswordView)


urlpatterns = router.urls
