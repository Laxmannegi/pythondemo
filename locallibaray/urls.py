from django.urls import path

from . import views

urlpatterns = [

	  path('', views.index, name='index'),
	  path('posts/', views.PostListView.as_view(), name='posts'),
]


# Add URLConf to create, update, and delete authors
