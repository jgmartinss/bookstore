from django.shortcuts import  get_object_or_404

from django.views import generic

from bookstore.apps.checkout.forms import CartAddProductForm

from . import models


class BookListView(generic.ListView):
    model = models.Book
    context_object_name = 'books'
    template_name = 'catalog/book/list.html'
    paginate_by = 9

    def get_queryset(self, **kwargs):
        return models.Book.objects.all().order_by('title')


class BookDetailView(generic.DetailView):
    model = models.Book
    context_object_name = 'book'
    template_name = 'catalog/book/detail.html'

    def get_object(self):
        _slug = self.kwargs.get("slug")
        return get_object_or_404(models.Book, slug=_slug)

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        bookreviews = models.BookReview.objects.all()
        bookimages = models.BookImages.objects.all()
        cart_product_form = CartAddProductForm()
        context['book_images'] = bookimages.filter(book=self.object)[:1]
        context['book_review'] = bookreviews.filter(book=self.object).order_by('-created')[:4]
        context['cart_product_form'] = cart_product_form
        return context


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
        context['books'] = models.Book.objects.filter(author=self.object)[:10]
        return context


class PublishingCompanyListView(generic.ListView):
    context_object_name = 'publishingcompany'
    model = models.PublishingCompany
    paginate_by = 15
    template_name = 'catalog/publishingcompany/list.html'

    def get_queryset(self, **kargs):
        return models.PublishingCompany.objects.all().order_by('name')