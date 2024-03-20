from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDeleteView, CategoryAPIView, TagAPIView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post_crud'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('tags/', TagAPIView.as_view(), name='tags'),
]
