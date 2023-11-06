from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Category, Articles

# Create your views here.

class CategoryListView(ListView):
    model=Category   

class ArticlesDetailView(DetailView):
    model=Articles
    
class ArticlesListView(ListView):
    model=Articles
    
# def homepage(request):
#     articles = Articles.objects.all()
#     return render(request, 'content/home.html', {'articles': articles})   

# def indexpage(request):
#     category = Category.objects.all()
#     article=category.Articles.all()
#     return render(request, 'content/index.html', {'category': category})  


    
# def category_detail(request, category_id):
#     category = Category.objects.get(id=category_id)
#     articles = category.Articles.all()

#     context = {
#         'category': category,
#         'articles': articles,
#     }

#     return render(request, 'category_detail.html', context)
    



        
        
        
 


    
     
     
        
    
    



# class CategoriesListView(ListView):
#     model = Categories
#     template_name = 'content/categories_list.html'
#     context_object_name = 'Category'

# class ArticleDetailView(DetailView):
#     model = Articles
#     template_name = 'article_detail.html'
#     context_object_name = 'article'

# class CategoryView(ListView):
#     template_name = 'category.html'
#     context_object_name = 'articles'

