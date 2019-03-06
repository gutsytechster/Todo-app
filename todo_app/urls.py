from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('tasks/', CreateView.as_view(), name='create'),
    path('tasks/<int:pk>/', DetailsView.as_view(), name='details'),
    path('users/', UserView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user-details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
