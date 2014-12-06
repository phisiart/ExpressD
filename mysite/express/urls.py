from django.conf.urls import patterns, url

from express import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<diner_id>\d+)$', views.order, name='order'),
    url(r'^o(?P<diner_id>\d+)$', views.list_orders, name='list_orders'),
    url(r'^send_order$', views.send_order, name='send_order'),
    url(r'^change_status$', views.change_status, name='change_status'),
)
