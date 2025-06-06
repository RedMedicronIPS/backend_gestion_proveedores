from django.urls import path
from .views import LoginView, RoleListCreateView, UserListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('roles/', RoleListCreateView.as_view(), name='roles'),
    path('users/', UserListView.as_view(), name='user-list'),
]
