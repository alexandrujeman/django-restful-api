from rest_framework import routers
from core import views as myapi_views

router = routers.DefaultRouter()
router.register(r'v1', myapi_views.ProjectDetail)
