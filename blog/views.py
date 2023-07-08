from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ArticleCreateForm
# Create your views here.


class ArticleCreateView(View):
    
    form_class = ArticleCreateForm
    initials = {'title': 'New Title', 'content': 'New content'}
    
    def get(self, request):
        form = self.form_class(initial=self.initials)
        return render(request, 'blog/article-create.html', {'form': form})
    
    def post(self, request):
        form = self.form_class(**request.POST)
        if form.is_valid():
            article = form.save()
            messages.add_message(request, messages.SUCCESS,
                                 f"{article.title} created!")
            return redirect('article_list')
        
        messages.add_message(request, messages.ERROR, "Invalid data!")
        return render(request, 'blog/article-create.html', {'form': form})