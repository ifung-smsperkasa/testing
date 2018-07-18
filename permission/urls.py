from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/$', views.category_list, name='category_list'),
    url(r'^input_category/$', views.input_category, name='input_category'),
    url(r'^permission/$', views.permission_list, name='permission_list'),
    url(r'^input_permission/$', views.input_permission, name='input_permission'),
    url(r'^delete_permission/?(?P<id>\d+)?/?$', views.delete_permission, name='delete_permission'),
    url(r'^logins/$',views.logins, name='logins'),
    url(r'^logouts/$',views.logouts, name='logouts'),
    url(r'^next_view/$',views.next_view, name='next_view'),
]
