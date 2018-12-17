from django.shortcuts import  get_object_or_404

from django.views import generic

from . import models



class BookListView(generic.ListView):
    model = models.Book
    context_object_name = 'books'
    template_name = 'catalog/book/list.html'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        return models.Book.objects.all().order_by('title')


class LastFourBookListView(generic.ListView):
    model = models.Book
    context_object_name = 'last_four_book'
    template_name = 'catalog/book/last_four.html'

    def get_queryset(self, **kargs):
        return models.Book.objects.all().order_by('-created')[:4]


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = 'catalog/book/detail.html'

    def get_object(self):
        _slug = self.kwargs.get("slug")
        return get_object_or_404(models.Book, slug=_slug)


class AuthorListView(generic.ListView):
    context_object_name = 'authors'
    model = models.Author
    paginate_by = 10
    template_name = 'catalog/author/list.html'

    def get_queryset(self, **kargs):
        return models.Author.objects.all().order_by('name')


class AuthorDetailView(generic.DetailView):
    model = models.Author
    context_object_name = 'author'
    template_name = 'catalog/author/detail.html'

    def get_object(self):
        _slug = self.kwargs.get("slug")
        return get_object_or_404(models.Author, slug=_slug)

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['books'] = models.Book.objects.filter(author=self.object)
        return context
