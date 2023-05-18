from django.urls import path
from .views import post_view ,post_detail ,main_view ,post_like
urlpatterns = [
    path('',main_view,name='main_view'),
    path('blog/',post_view,name='post_view'),
    path('<int:pk>/',post_detail , name='post_detail'),
    path('like/<int:post_id>/',post_like , name='post_like'),
]
