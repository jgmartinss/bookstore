from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('customer/', views.AccountView.as_view(), name='detail'),
    path('customer/<str:token>/edit/', views.AccountUpdateView.as_view(), name='edit'),
    path('customer/address/new/', views.AddressCreateView.as_view(), name='new-address'),
    path('customer/address/list/', views.AddressListView.as_view(), name='list-address'),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
