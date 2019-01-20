from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bookstore.apps.catalog.views import (
    BookListView,
    BookDetailView,
    AuthorListView,
    AuthorDetailView,
    PublishingCompanyListView,
)


app_name = "catalog"

urlpatterns = [
    path(
        "books/", 
        BookListView.as_view(), 
        name="book-list"
    ),
    path(
        "book/<slug:slug>/", 
        BookDetailView.as_view(), 
        name="book-detail"
    ),
    path(
        "authors/", 
        AuthorListView.as_view(), 
        name="author-list"
    ),
    path(
        "author/<slug:slug>/", 
        AuthorDetailView.as_view(), 
        name="author-detail"
    ),
    path(
        "publishingcompanies/",
        PublishingCompanyListView.as_view(),
        name="publishing-list",
    ),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
