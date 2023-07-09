from django.urls import path
from .views import ArticleCreateView, ArticleDetailView, ArticleListView, ArticleDeleteView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('list/', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]