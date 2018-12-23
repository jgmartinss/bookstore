from django.urls import path

from django.utils.translation import gettext_lazy as _

from . import views


urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    #path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
]
