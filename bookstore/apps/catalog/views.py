from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView

from bookstore.apps.checkout.forms import CartAddProductForm
from bookstore.apps.catalog.models import (
    Book,
    Author,
    PublishingCompany,
    BookReview,
    BookImages,
    AuthorImages,
)


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 9
    template_name = "catalog/book/list.html"

    def get_queryset(self, **kwargs):
        return Book.objects.all().order_by("title")


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "catalog/book/detail.html"

    def get_object(self):
        _slug = self.kwargs.get("slug")
        return get_object_or_404(Book, slug=_slug)

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context["book_images"] = BookImages.objects.filter(book=self.object)[:1]
        context["book_review"] = BookReview.objects.filter(book=self.object).order_by(
            "-created"
        )[:4]
        context["cart_product_form"] = CartAddProductForm()
        return context


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    paginate_by = 10
    template_name = "catalog/author/list.html"

    def get_queryset(self, **kargs):
        return Author.objects.all().order_by("name")


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = "catalog/author/detail.html"

    def get_object(self):
        _slug = self.kwargs.get("slug")
        return get_object_or_404(Author, slug=_slug)

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.object)[:10]
        context["author_images"] = AuthorImages.objects.filter(author=self.object)[:1]
        return context


class PublishingCompanyListView(ListView):
    model = PublishingCompany
    context_object_name = "publishingcompany"
    paginate_by = 15
    template_name = "catalog/publishingcompany/list.html"

    def get_queryset(self, **kargs):
        return PublishingCompany.objects.all().order_by("name")
