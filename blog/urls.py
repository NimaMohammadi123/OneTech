from django.urls import path
from .views import post_view ,post_detail
urlpatterns = [
    path('',post_view,name='post_view'),
    path('<int:id_post>/',post_detail , name='post_detail'),
]
