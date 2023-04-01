from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/create/', views.brand_create, name='brand_create'),
    path('brand/<int:brand_pk>/', views.brand_update, name='brand_update'),
    path('publish/post/', views.publish_post, name='publish_post'),
    path('publish/blog/', views.publish_blog, name='publish_blog'),

]