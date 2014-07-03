from django.conf.urls import patterns, include, url
from garden_app import views

urlpatterns = patterns('',
	url(r'^users/$',views.users, name='users'),


)