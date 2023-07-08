from django.urls import path
from .views import ArticleCreateView, ArticleDetailView, ArticleListView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('list/', ArticleListView.as_view(), name='article_create'),
    path('detail/<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
]