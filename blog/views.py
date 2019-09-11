from django.shortcuts import get_list_or_404, get_object_or_404
# from django.http import HttpResponse
from .models import Article, Categorie
from django.views.generic import ListView, DetailView


# Create your views here.
# Generic Views to display articles views

class PostListView(ListView):
    model = Article
    context_object_name = 'posts'
    template_name = 'blog/home_page.html'
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        return Article.objects.filter(valide=True).order_by('-date_post')

    def get_context_data(self, **kwargs):
        # Call the super classe to get context
        context = super().get_context_data(**kwargs)

        # Add {{all}} variable to context
        context['all'] = 'w3-black'
        return context


class CategorieListView(ListView):
    model = Article
    context_object_name = 'posts'
    template_name = 'blog/home_page.html'
    paginate_orphans = 5
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs['categorie']:
            categorie = Categorie.objects.get(nom=self.kwargs['categorie'])
            return Article.objects.filter(categorie=categorie, valide=True)
        else:
            return Article.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the QuerySet the categorie name if it gave
        if self.kwargs['categorie']:
            context['categorie_name'] = self.kwargs['categorie']
            if self.kwargs['categorie'] == 'Developpeur':
                context['dev'] = 'w3-black'
            elif self.kwargs['categorie'] == 'Demarreur':
                context['dem'] = 'w3-black'
            elif self.kwargs['categorie'] == 'autres':
                context['autres'] = 'w3-black'
            else:
                context['all'] = 'w3-black'
        return context


# Post DetailView
class PostDetailView(DetailView):
    model = Article
    context_object_name = 'post'
    template_name = 'blog/post_content.html'
