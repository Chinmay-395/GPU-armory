from django.urls import path
from . import views
from gpuApi.views import GpuViewset
# from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', GpuViewset, basename='gpu')
urlpatterns = router.urls
# urlpatterns = [
#     # path('', views.apiOverview, name="api-overview"),
#     # path('item-list/', views.itemList, name="item-list"),
#     # path('item-detail/<str:pk>/', views.itemDetail, name="item-detail"),
#     path('', GpuRetrieveApiView.as_view(), name='gpuList'),
# ]
