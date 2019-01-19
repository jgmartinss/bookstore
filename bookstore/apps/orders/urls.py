from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bookstore.apps.orders.views import OrderListView, OrderDetailView


app_name = "orders"

urlpatterns = [
    path(
        "history/", 
        OrderListView.as_view(), 
        name="list-order"
    ),
    path(
        "<int:id>/detail/", 
        OrderDetailView.as_view(), 
        name="detail"
    ),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
