from rest_framework.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView


urlpatterns = [
    path(
        'users',
        UserListCreateView.as_view(),
        name='users-list-create'
    ),
    path(
        'users/<int:id>',
        UserRetrieveUpdateDestroyView.as_view(),
        name='users-detail'
    )
]