from django.conf.urls import url
from permission import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import PerizinanViewSet,CategoryViewSet

router = DefaultRouter()
router.register('perizinan',PerizinanViewSet)
router.register('category',CategoryViewSet)
schema_view = get_swagger_view(title='Perizinan',url='/')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'^perizinan/$', views.PerizinanList.as_view()),
    # url(r'^perizinan/(?P<pk>[0-9]+)/$', views.PerizinanDetail.as_view()),
    url(r'^docs/$', schema_view),
]
