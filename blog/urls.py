from django.urls import path
from .views import HomepageView, PostDetailsView, CreatePostView, PostUpdateView, DeletePostView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('details/<int:pk>/', PostDetailsView.as_view(), name='detail'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
]
