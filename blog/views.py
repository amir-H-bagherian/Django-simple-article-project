from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from .forms import ArticleCreateForm
from .models import Article
# Create your views here.


class ArticleCreateView(View):
    
    form_class = ArticleCreateForm
    initials = {'title': 'New Title', 'content': 'New content'}
    
    def get(self, request):
        form = self.form_class(initial=self.initials)
        return render(request, 'blog/article-create.html', {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            article = form.save()
            messages.add_message(request, messages.SUCCESS,
                                 f"{article.title} created!")
            return redirect('article_list')
        
        messages.add_message(request, messages.ERROR, "Invalid data!")
        return render(request, 'blog/article-create.html', {'form': form})
    
class ArticleListView(View):
    model = Article
    
    def get(self, request):
        context = {
            'articles': self.model.objects.all()
        }
        return render(request, 'blog/article-list.html', context)
    
class ArticleDetailView(View):
    model = Article
    
    def get(self, request, pk):
        context = {
            'article': get_object_or_404(self.model, pk=pk)
        }
        return render(request, 'blog/article-detail.html', context)
    
class ArticleDeleteView(View):
    model = Article
    
    def get(self, request, pk):
        context = {
            'article': get_object_or_404(self.model, pk=pk)
        }
        return render(request, 'blog/article-delete.html', context)
    
    def post(self, request, pk):
        article = get_object_or_404(self.model, pk=pk)
        article.delete()
        return redirect('article_list')
        