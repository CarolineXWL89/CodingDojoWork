from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index), #nothing after 1st space --> root page
	url(r'^test/', views.test)
]