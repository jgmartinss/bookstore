from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from bookstore.apps.accounts.views import (
    LoginView,
    RegisterView,
    LogoutView,
    AccountView,
    AccountUpdateView,
    AddressCreateView,
    AddressListView,
    AddressDeleteView,
    AddressUpdateView,
)


app_name = "accounts"

urlpatterns = [
    path(
        "login/", 
        LoginView.as_view(), 
        name="login"
    ),
    path(
        "register/", 
        RegisterView.as_view(), 
        name="register"
    ),
    path(
        "logout/", 
        LogoutView.as_view(), 
        name="logout"
    ),
    path(
        "customer/", 
        AccountView.as_view(), 
        name="detail"
    ),
    path(
        "customer/<str:token>/edit/", 
        AccountUpdateView.as_view(), 
        name="edit"
    ),
    path(
        "customer/address/new/", 
        AddressCreateView.as_view(), 
        name="new-address"
    ),
    path(
        "customer/address/list/", 
        AddressListView.as_view(), 
        name="list-address"
    ),
    path(
        "customer/address/<int:id>/del/",
        AddressDeleteView.as_view(),
        name="del-address",
    ),
    path(
        "customer/address/<int:id>/edit/",
        AddressUpdateView.as_view(),
        name="edit-address"
    ),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
