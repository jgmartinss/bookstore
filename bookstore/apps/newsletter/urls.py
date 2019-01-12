from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


app_name = "newsletter"

urlpatterns = [
	path(
		"new/", 
		views.SubscribeCreateView.as_view(), 
		name="new-newsletter"
	),
	path(
		"list/", 
		views.MyNewsletterListView.as_view(), 
		name="list-newsletter"
	),
	path(
		"<int:id>/del/", 
		views.NewsletterDeleteView.as_view(), 
		name="del-newsletter"
	),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
