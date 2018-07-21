from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/$', views.ListCategoryView.as_view(), name='category_list'),
    url(r'^input_category/$', views.InputCategory.as_view(), name='input_category'),
    url(r'^permission/$', views.ListPerizinanView.as_view(), name='permission_list'),
    url(r'^input_permission/$', views.InputPerizinan.as_view(), name='input_permission'),
    url(r'^delete_permission/?(?P<pk>\d+)?/?$', views.DeletePerizinan.as_view(), name='delete_permission'),
    url(r'^logins/$',views.Login_.as_view(template_name = 'permission/login.html'), name='logins'),
    url(r'^logouts/$',views.logouts, name='logouts'),
    url(r'^update_permission/?(?P<pk>\d+)?/?$', views.UpdatePerizinan.as_view(),name='update_permission'),
    url(r'^detail_permission/?(?P<pk>\d+)?/?$', views.DetailEmployee.as_view(),name='detail_permission'),
]
