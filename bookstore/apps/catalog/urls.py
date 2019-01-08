from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


app_name = "catalog"

urlpatterns = [
    path(
    	"books/", 
    	views.BookListView.as_view(), 
    	name="book-list"
    ),
    path(
    	"book/<slug:slug>/", 
    	views.BookDetailView.as_view(), 
    	name="book-detail"
    ),
    path(
    	"authors/", 
    	views.AuthorListView.as_view(), 
    	name="author-list"
    ),
    path(
    	"author/<slug:slug>/", 
    	views.AuthorDetailView.as_view(), 
    	name="author-detail"
    ),
    path(
        "publishingcompanies/",
        views.PublishingCompanyListView.as_view(),
        name="publishing-list",
    ),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
