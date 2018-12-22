from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views import generic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('bookstore.apps.accounts.urls')),
    path('catalog/', include('bookstore.apps.catalog.urls')),
    path('checkout/', include('bookstore.apps.checkout.urls')),
    path('trumbowyg/', include('trumbowyg.urls')),
    path('', generic.TemplateView.as_view(template_name='index.html'), name='index'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
