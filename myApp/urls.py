
from django.urls import path
from .views import user_list, user_detail

urlpatterns = [
    path('users/', user_list),
    path('details/<str:username>', user_detail),
]
