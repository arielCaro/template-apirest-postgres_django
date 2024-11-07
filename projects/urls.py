from rest_framework import routers
from .api import ProjectViewSet, UserViewSet, RoleViewSet, CompanyViewSet, SessionViewSet
router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/users', UserViewSet, 'users')
router.register('api/roles', RoleViewSet, 'roles')
router.register('api/companies', CompanyViewSet, 'companies')
router.register('api/sessions', SessionViewSet, 'sessions')
urlpatterns = router.urls