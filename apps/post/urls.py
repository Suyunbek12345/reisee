from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet, WorkViewSet

router = DefaultRouter()
router.register('registrations', RegistrationViewSet, 'registration')
router.register('works', WorkViewSet, 'work')

urlpatterns = []


urlpatterns += router.urls
